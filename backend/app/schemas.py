from pydantic import BaseModel

#se definen los campos obligatorios
class NoteCreate(BaseModel):
    title: str
    content: str

class Note(NoteCreate):
    id: int

    class Config:
        from_attributes = True


