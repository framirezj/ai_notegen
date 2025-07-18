from pydantic import BaseModel, EmailStr

#notes

#se definen los campos obligatorios
class NoteCreate(BaseModel): #in
    title: str
    content: str

class Note(NoteCreate): #out
    id: int

    class Config:
        from_attributes = True


#users
class UserCreate(BaseModel): #in
    email: EmailStr
    password: str

class UserOut(BaseModel): #out
    id: int
    email: EmailStr

    class Config:
        from_attributes = True
