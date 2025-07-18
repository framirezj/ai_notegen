from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from .. import models, schemas
from ..database import get_db

router = APIRouter(
    tags=["Notes"],
    prefix="/notes"  # Todas las rutas aquí comenzarán con /notes
)

#rutas

#el argumento response_model=schemas.Note,  dice a FastAPI que la respuesta debe tener la estructura del modelo Note (usando Pydantic para validación y serialización)
@router.post("/", response_model=schemas.Note, status_code=status.HTTP_201_CREATED)
def create_note(note: schemas.NoteCreate, db: Session = Depends(get_db)):
    # Creamos una instancia de Note con los datos del body
    db_note = models.Note(**note.model_dump())
    db.add(db_note)
    db.commit()
    # Refrescamos para obtener el ID asignado por la base de datos
    db.refresh(db_note)
    return db_note


@router.get("/", response_model=list[schemas.Note]) #le diremos a fastapi que va salir y sera una lista de objetos de Note
def get_notes(db: Session = Depends(get_db)):
    #ocupamos el metodo query de la Session a la bd y traemos todos los registros de la tabla Note
    return db.query(models.Note).all()


@router.delete("/{note_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_note(note_id: int ,db: Session = Depends(get_db)):
    db_note = db.query(models.Note).filter(models.Note.id == note_id).first()

    if not db_note:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Nota no encontrada")
    db.delete(db_note)
    db.commit()

#recibiremos un id y responderemos con un objeto tipo nota a json
@router.put("/{note_id}", response_model=schemas.Note)
def update_note(note_id: int, note: schemas.NoteCreate , db: Session = Depends(get_db)):
    
    db_note = db.query(models.Note).filter(models.Note.id == note_id).first()
    
    if not db_note:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Nota no encontrada")
    
    # model_dump convierte el objeto note a diccionario
    # items devuelve el formato clave valor
    for key, value in note.model_dump().items():
        setattr(db_note, key, value)

    db.commit()
    db.refresh(db_note) # Actualiza el objeto en la sesión
    return db_note      # Devuelve el objeto ya actualizado