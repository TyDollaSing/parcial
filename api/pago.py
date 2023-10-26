from flask import Blueprint, request, jsonify, json
from config.db import db, app, ma
from models.pago import Pago, PagoSchema
from models.pasajero import Pasajero, PasajeroSchema

ruta_pago = Blueprint("ruta_pago", __name__)

pago_schema = PagoSchema()
pagos_schema = PagoSchema(many=True)


@ruta_pago.route("/pago", methods=["GET"])
def pago():
    resultall = Pago.query.all()
    resultado_pago = pagos_schema.dump(resultall)
    return jsonify(resultado_pago)


@ruta_pago.route("/savepago", methods=["POST"])
def save():
    idpasajero = request.json["idpasajero"]
    montoTotal = request.json["monto"]
    fechaPago = request.json["fecha"]
    metodoPago = request.json["metodo"]
    new_pago = Pago(
        idpasajero,
        montoTotal,
        fechaPago,
        metodoPago,
    )
    db.session.add(
        new_pago,
    )
    db.session.commit()
    return "Datos guardado con exito"


@ruta_pago.route("/updatepago", methods=["PUT"])
def Update():
    id = request.json["id"]
    idpasajero = request.json["idpasajero"]
    montoTotal = request.json["monto"]
    fechaPago = request.json["fecha"]
    metodoPago = request.json["metodo"]
    pago = Pago.query.get(id)
    if pago:
        print(pago)
        pago.idpasajero = idpasajero
        pago.monto_total = montoTotal
        pago.fecha_pago = fechaPago
        pago.metodo_pago = metodoPago
        db.session.commit()
        return "Datos actualizados con exitos"
    else:
        return "Error :/ "


@ruta_pago.route("/deletepago/<id>", methods=["DELETE"])
def eliminar(id):
    pago = Pago.query.get(id)
    db.session.delete(pago)
    db.session.commit()
    return jsonify(
        pago_schema.dump(pago),
    )


@ruta_pago.route("/relacionpasajero", methods=["POST"])
def dostabla():
    datos = {}
    resultado = db.session.query(Pasajero, Pago).select_from(Pasajero).join(Pago).all()
    i = 0
    for pasajero, pago in resultado:
        i += 1
        datos[i] = {
            "pasajero": pasajero.id,
            # "pago": pago.id,
        }
    return datos
