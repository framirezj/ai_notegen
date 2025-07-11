from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import models, schemas, database


router = APIRouter()

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()



#rutas

#el argumento response_model=schemas.Note,  dice a FastAPI que la respuesta debe tener la estructura del modelo Note (usando Pydantic para validación y serialización)
@router.post("/notes/", response_model=schemas.Note)
def create_note(note: schemas.NoteCreate, db: Session = Depends(get_db)):

    #creamos una instancia de Note
    db_note = models.Note(title = note.title, content = note.content)
    #agregamos la nota
    db.add(db_note)
    #confirmamos
    db.commit()
    #trae la nota que se guardo con el id....
    db.refresh(db_note)
    #retorna el dato
    return db_note


@router.get("/notes", response_model=list[schemas.Note]) #le diremos a fastapi que va salir y sera una lista de objetos de Note
def get_notes(db: Session = Depends(get_db)):
    #ocupamos el metodo query de la Session a la bd y traemos todos los registros de la tabla Note
    return db.query(models.Note).all()


@router.delete("/notes/{note_id}", status_code=204)
def delete_note(note_id: int ,db: Session = Depends(get_db)):
    db_note = db.query(models.Note).filter(models.Note.id == note_id).first()
    if not db_note:
        raise HTTPException(status_code=404, detail="Note not found")
    db.delete(db_note)
    db.commit()

#recibiremos un id y responderemos con un objeto tipo nota a json
@router.put("/notes/{note_id}", response_model=schemas.Note)

def update_note(note_id: int, note: schemas.NoteCreate , db: Session = Depends(get_db)):
    
    db_note = db.query(models.Note).filter(models.Note.id == note_id).first()
    
    if not db_note:
        raise HTTPException(status_code=404, detail="Note not found")
    
    db_note.title = note.title
    db_note.content = note.content

    db.commit()

    db.refresh(db_note) # Actualiza el objeto en la sesión
    return db_note      # Devuelve el objeto ya actualizado
