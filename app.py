from flask import Flask, jsonify, json
from config.db import db, ma, app

from api.vehiculo import Vehiculo, ruta_vehiculo
from api.reporte import Reporte, ruta_reporte
from api.pasajero import Pasajero, ruta_pasajero
from api.viaje import Viaje, ruta_viaje
from api.solicitud import Solicitud, ruta_solicitud
from api.pago import Pago, ruta_pago

app.register_blueprint(ruta_pasajero, url_prefix="/parcial")
app.register_blueprint(ruta_reporte, url_prefix="/parcial")
app.register_blueprint(ruta_viaje, url_prefix="/parcial")
app.register_blueprint(ruta_pago, url_prefix="/parcial")
app.register_blueprint(ruta_vehiculo, url_prefix="/parcial")
app.register_blueprint(ruta_solicitud, url_prefix="/parcial")

@app.route("/")
def hello():
    return "Hello World!"


if __name__ == "__main__":
    app.run(debug=True, port=5000, host="0.0.0.0")