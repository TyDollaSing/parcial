from flask import Blueprint, request, jsonify, json
from config.db import db, app, ma
from models.pasajero import Pasajero, PasajeroSchema

ruta_pasajero = Blueprint("ruta_pasajero", __name__)

pasajero_schema = PasajeroSchema()
pasajeros_schema = PasajeroSchema(many=True)


@ruta_pasajero.route("/pasajero", methods=["GET"])
def pasajero():
    resultall = Pasajero.query.all()
    resultado_pasajero = pasajeros_schema.dump(resultall)
    return jsonify(resultado_pasajero)


@ruta_pasajero.route("/savepasajero", methods=["POST"])
def save():
    nombre = request.json["nombre"]
    apellido = request.json["apellido"]
    email = request.json["correo"]
    tel = request.json["telefono"]
    dir = request.json["direccion"]
    new_pago = Pasajero(
        nombre,
        apellido,
        email,
        tel,
        dir,
    )
    db.session.add(
        new_pago,
    )
    db.session.commit()
    return "Datos guardados con exito"


@ruta_pasajero.route("/updatepasajero", methods=["PUT"])
def Update():
    idPasajero = request.json["id"]
    nombre = request.json["nombre"]
    apellido = request.json["apellido"]
    email = request.json["correo"]
    tel = request.json["telefono"]
    dir = request.json["direccion"]
    pasajero = Pasajero.query.get(idPasajero)
    if pasajero:
        print(pasajero)
        pasajero.nombre = nombre
        pasajero.apellido = apellido
        pasajero.correo_electronico = email
        pasajero.telefono = tel
        pasajero.direccion = dir
        db.session.commit()
        return "Datos actualizados con exitos"
    else:
        return "Error :/ "


@ruta_pasajero.route("/deletepasajero/<id>", methods=["DELETE"])
def eliminar(id):
    pasajero = Pasajero.query.get(id)
    db.session.delete(pasajero)
    db.session.commit()
    return jsonify(
        pasajero_schema.dump(pasajero),
    )
