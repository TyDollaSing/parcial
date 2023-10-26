from config.db import db, ma, app


class Vehiculo(db.Model):
    __tablename__ = "tblvehiculo"

    id = db.Column(db.Integer, primary_key=True)
    placa = db.Column(db.String(50))
    modelo = db.Column(db.String(50))  
    estado = db.Column(db.String(50)) 
    capacidad = db.Column(db.String(50))

    def __init__(
        self,
        placa,
        modelo,
        estado,
        capacidad,
    ):
        self.placa = placa
        self.modelo = modelo
        self.estado = estado
        self.capacidad = capacidad


with app.app_context():
    db.create_all()


class VehiculoSchema(ma.Schema):
    class Meta:
        fields = (
            "id",
            "placa",
            "modelo",
            "estado",
            "capacidad",
        )