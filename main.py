from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
import firestore

APP = FastAPI()

class Usuario(BaseModel):
    nickname: str
    email: str
    edad: Optional[int]    

#Ruta raiz de la api
#Las rutas funcionan de la siguiente manera, al crear un ruta esta ejecutara la funcion que contenga debajo
@APP.get("/")
def index():
    return {"Titulo": "Usuarios pokefit API"}

@APP.get("/usuarios/")
def mostrarUsuarios():
    return firestore.obtener_usuarios()

@APP.post("/usuarios/")
def agregarUsuario(usuario: Usuario):
    return firestore.agregar_usuario(usuario)