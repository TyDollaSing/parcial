from config.db import db, ma, app


class Solicitud(db.Model):
    __tablename__ = "tblsolicitud"

    id = db.Column(db.Integer, primary_key=True)
    idviaje= db.Column(db.Integer, db.ForeignKey("tblviaje.id"))
    origen = db.Column(db.String(50))
    destino = db.Column(db.String(50))
    estado = db.Column(db.String(50)) 
    hora = db.Column(db.String(50))

    def __init__(
        self,
        idviaje,
        origen,
        destino,
        estado,
        hora,
    ):
        self.idviaje = idviaje
        self.origen = origen
        self.destino = destino
        self.estado = estado
        self.hora = hora


with app.app_context():
    db.create_all()


class SolicitudSchema(ma.Schema):
    class Meta:
        fields = (
            "id",
            "idviaje",
            "origen",
            "destino",
            "estado",
            "hora",
        )
