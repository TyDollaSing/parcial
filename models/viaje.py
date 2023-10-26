from config.db import db, ma, app


class Viaje(db.Model):
    __tablename__ = "tblviaje"

    id = db.Column(db.Integer, primary_key=True)
    idpasajero = db.Column(db.Integer, db.ForeignKey("tblpasajero.id"))
    idvehiculo = db.Column(db.Integer, db.ForeignKey("tblvehiculo.id"))
    horai = db.Column(db.String(200))
    horaf = db.Column(db.String(200))
    ruta = db.Column(db.String(200))

    def __init__(
        self,
        idpasajero,
        idvehiculo,
        horai,
        horaf,
        ruta,
    ):
        self.idpasajero = idpasajero
        self.idvehiculo = idvehiculo
        self.horai = horai
        self.horaf = horaf
        self.ruta = ruta


with app.app_context():
    db.create_all()


class ViajeSchema(ma.Schema):
    class Meta:
        fields = (
            "id",
            "idpasajero",
            "idvehiculo",
            "horai",
            "horaf",
            "ruta",
        )
