import uuid
import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate("key.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

def obtener_usuarios():
    usuarios = []
    docs = db.collection("Users").stream()
    for doc in docs:
        datos = doc.to_dict()
        usuarios.append([datos["uid"],datos["email"], datos["nickname"], datos["edad"]])
    
    return usuarios

def agregar_usuario(usuario):

    uid = str(uuid.uuid4());

    db.collection("Users").document(uid).set({
        "nickname": usuario.nickname,
        "email": usuario.email,
        "edad": usuario.edad,
        "uid": uid
    })
    return {"Mensaje": "Usuario agregado"}