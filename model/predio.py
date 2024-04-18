from utils.db import db
from dataclasses import dataclass

@dataclass
class Predio(db.Model):
    id_predio: int
    id_tipo_predio: int
    descripcion: str
    ruc: str
    correo: str
    telefono: str
    direccion: str
    idubigeo: str
    id_persona: int
    url_imagen: str

    id_predio= db.Column(db.Integer, primary_key=True)
    id_tipo_predio=db.Column(db.Integer)
    descripcion= db.Column(db.String(80))
    ruc=db.Column(db.String(20))
    correo= db.Column(db.String(80))
    telefono= db.Column(db.String(12))
    direccion= db.Column(db.String(100))
    idubigeo= db.Column(db.String(6))
    id_persona= db.Column(db.Integer)
    url_imagen= db.Column(db.String(120))



    def __init__(self,id_tipo_predio, descripcion, ruc, correo, telefono, direccion,idubigeo,id_persona,url_imagen ):
        self.id_tipo_predio= id_tipo_predio
        self.descripcion= descripcion
        self.ruc= ruc
        self.correo= correo
        self.telefono= telefono  
        self.direccion= direccion  
        self.idubigeo= idubigeo  
        self.id_persona= id_persona  
        self.url_imagen= url_imagen  


        