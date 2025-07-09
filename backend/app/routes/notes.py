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

    
