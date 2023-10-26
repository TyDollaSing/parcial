from config.db import db, ma, app


class Reporte(db.Model):
    __tablename__ = "tblreporte"

    id = db.Column(db.Integer, primary_key=True)
    tipo = db.Column(db.String(100))  
    fecha = db.Column(db.String(100))
    estado = db.Column(db.String(100))
    contenido = db.Column(db.String(100))

    def __init__(
        self,
        tipo,
        fecha,
        estado,
        contenido,
    ):
        self.tipo = tipo
        self.fecha = fecha
        self.estado = estado
        self.contenido = contenido


with app.app_context():
    db.create_all()


class ReporteSchema(ma.Schema):
    class Meta:
        fields = (
            "id",
            "tipo_reporte",
            "fecha",
            "estado",
            "contenido",
        )