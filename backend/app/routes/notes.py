from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from .. import models, schemas
from ..database import get_db
from ..auth import get_current_user

router = APIRouter(
    tags=["Notes"],
    prefix="/notes",  # Todas las rutas aquí comenzarán con /notes
    dependencies=[Depends(get_current_user)] # Aplica autenticación a todas las rutas de este router
)

#rutas

#el argumento response_model=schemas.Note,  dice a FastAPI que la respuesta debe tener la estructura del modelo Note (usando Pydantic para validación y serialización)
@router.post("/", response_model=schemas.NoteOut, status_code=status.HTTP_201_CREATED)
def create_note(note: schemas.NoteCreate, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    # Creamos una instancia de Note con los datos del body y ademas le enviamos el id del usuario autenticado
    db_note = models.Note(**note.model_dump(), user_id = current_user.id)
    db.add(db_note)
    db.commit()
    # Refrescamos para obtener el ID asignado por la base de datos
    db.refresh(db_note)
    return db_note


@router.get("/", response_model=list[schemas.NoteOut]) #le diremos a fastapi que va salir y sera una lista de objetos de Note
def get_notes(db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    # Obtenemos solo las notas que pertenecen al usuario actual
    return db.query(models.Note).filter(models.Note.user_id == current_user.id).all()


@router.delete("/{note_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_note(note_id: int ,db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    note_query = db.query(models.Note).filter(models.Note.id == note_id)
    db_note = note_query.first()

    if not db_note:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Nota no encontrada")

    if db_note.user_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="No tienes permiso para eliminar esta nota")

    note_query.delete(synchronize_session=False)
    db.commit()

#recibiremos un id y responderemos con un objeto tipo nota a json
@router.put("/{note_id}", response_model=schemas.NoteOut)
def update_note(note_id: int, note: schemas.NoteCreate , db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    
    note_query = db.query(models.Note).filter(models.Note.id == note_id)
    db_note = note_query.first()
    
    #La nota
    if not db_note:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Nota no encontrada")
    
    #el usuario
    if db_note.user_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="No tienes permiso para editar esta nota")

    # model_dump convierte el objeto note a diccionario
    # items devuelve el formato clave valor
    for key, value in note.model_dump().items():
        setattr(db_note, key, value)

    db.commit()
    db.refresh(db_note) # Actualiza el objeto en la sesión para obtener los datos actualizados
    return db_note