from app import db

class Solicitud(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(20), nullable=False)
    apellido = db.Column(db.String(20), nullable=False)
    identificacion = db.Column(db.String(10), nullable=False, unique=True)
    edad = db.Column(db.Integer, nullable=False)
    afinidad_magica = db.Column(db.String(20), nullable=False)
    estatus = db.Column(db.String(20), default="pendiente")

    def to_dict(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'apellido': self.apellido,
            'identificacion': self.identificacion,
            'edad': self.edad,
            'afinidad_magica': self.afinidad_magica,
            'estatus': self.estatus
        }    

class Grimorio(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tipo = db.Column(db.String(20), nullable=False)
    estudiante_id = db.Column(db.Integer, db.ForeignKey('solicitud.id'), nullable=False)
    estudiante = db.relationship('Solicitud', backref=db.backref('grimorio', uselist=False))

    def to_dict(self):
        return {
            'id': self.id,
            'tipo': self.tipo,
            'estudiante_id': self.estudiante_id,
            'estudiante': self.estudiante.to_dict() if self.estudiante else None
        }
