from config.db import db, ma, app


class Pago(db.Model):
    __tablename__ = "tblpago"

    id = db.Column(db.Integer, primary_key=True)
    idpasajero = db.Column(db.Integer, db.ForeignKey("tblpasajero.id"))
    monto = db.Column(db.String(200))
    fecha = db.Column(db.String(200))
    metodo = db.Column(db.String(200))

    def __init__(self, idpasajero, monto, fecha, metodo):
        self.idpasajero = idpasajero
        self.monto = monto
        self.fecha = fecha
        self.metodo = metodo


with app.app_context():
    db.create_all()


class PagoSchema(ma.Schema):
    class Meta:
        fields = (
            "id",
            "idpasajero",
            "monto",
            "fecha",
            "metodo",
        )
