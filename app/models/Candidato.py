from app import db
from app import ma

class Candidato(db.Model):
    __tablename__ = 'candidato'
    id_candidato  = db.Column(db.Integer, primary_key=True)
    nombres = db.Column(db.String(100), nullable=False)
    apellido_paterno = db.Column(db.String(100), nullable=False)
    apellido_materno = db.Column(db.String(100), nullable=False)
    denegado = db.Column(db.Boolean, nullable=True, default=False)
    rol = db.Column(db.String(100), nullable=False)
    id_lista = db.Column(db.Integer, db.ForeignKey('listacandidato.id_lista'),nullable=True)

    lista_candidato = db.relationship('ListaCandidato', backref='candidatos_list', lazy=True)
    
    def __init__(self, nombres, apellido_paterno, apellido_materno,rol, id_lista_candidato,denegado=False):
        self.nombres = nombres
        self.apellido_paterno = apellido_paterno
        self.apellido_materno = apellido_materno
        self.denegado = denegado
        self.rol = rol
        self.id_lista = id_lista_candidato
    
class CandidatoSchema(ma.Schema):
    class Meta:
        fields = (
            'id_candidato',
            'nombres',
            'apellido_paterno',
            'apellido_materno',
            'denegado',
            'rol',
            'id_lista'
        )