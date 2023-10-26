from flask import Blueprint, request, jsonify, json
from config.db import db, app, ma
from models.viaje import Viaje, ViajeSchema
from models.pasajero import Pasajero, PasajeroSchema
from models.vehiculo import Vehiculo, VehiculoSchema
ruta_viaje = Blueprint("ruta_viaje", __name__)

viaje_schema = ViajeSchema()
viajes_schema = ViajeSchema(many=True)


@ruta_viaje.route("/viaje", methods=["GET"])
def viaje():
    resultall = Viaje.query.all()
    resultado_viaje = viajes_schema.dump(resultall)
    return jsonify(resultado_viaje)


@ruta_viaje.route("/saveviaje", methods=["POST"])
def save():
    idpasajero = request.json["idpasajero"]
    idvehiculo = request.json["idvehiculo"]
    hora_inicio = request.json["hora_inicio"]
    hora_fin = request.json["hora_fin"]
    ruta = request.json["ruta"]
    estado = request.json["estado"]
    new_viaje = Viaje(
        idpasajero,
        idvehiculo,
        hora_inicio,
        hora_fin,
        ruta,
        estado,
    )
    db.session.add(
        new_viaje,
    )
    db.session.commit()
    return "Datos guardado con exito"

@ruta_viaje.route("/updateviaje", methods=["PUT"])
def Update():
    id = request.json["id"]
    idPasajero = request.json["idpasajero"]
    idVehiculo = request.json["idvehiculo"]
    hora_inicio = request.json["hora_inicio"]
    hora_fin = request.json["hora_fin"]
    ruta = request.json["ruta"]
    estado = request.json["estado"]
    pago = Viaje.query.get(id)
    if pago:
        print(pago)
        pago.idpasajero = idPasajero
        pago.idvehiculo = idVehiculo
        pago.hora_inicio = hora_inicio
        pago.hora_fin = hora_fin
        pago.ruta = ruta
        pago.estado = estado
        db.session.commit()
        return "Datos actualizados con exitos"
    else:
        return "Error :/ "
    
@ruta_viaje.route("/deletepago/<id>", methods=["DELETE"])
def eliminar(id):
    pago = Viaje.query.get(id)
    db.session.delete(pago)
    db.session.commit()
    return jsonify(
        viaje_schema.dump(pago),
    )

@ruta_viaje.route("/Relacion", methods=["POST"])
def dostabla():
    datos = {}
    resultado = (
        db.session.query(Pasajero, Vehiculo, Viaje).select_from(Pasajero).join(Viaje).all()
    )
    i = 0
    for pasajero, vehiculo, viaje in resultado:
        i += 1
        datos[i] = {
            "pasajero": pasajero.id,
            "vehiculo": vehiculo.id,
            "viaje": viaje.id
            # "pago": pago.id,
        }
    return datos