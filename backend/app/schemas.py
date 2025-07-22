from pydantic import BaseModel, EmailStr

#notes

#se definen los campos obligatorios
class NoteBase(BaseModel): #in
    title: str
    content: str

class NoteCreate(NoteBase):
    user_id: int

class NoteOut(NoteBase): #out
    id: int
    user_id: int


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
