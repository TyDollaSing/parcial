from flask import Blueprint, request, jsonify, json
from config.db import db, app, ma
from models.vehiculo import Vehiculo, VehiculoSchema

ruta_vehiculo = Blueprint("ruta_vehiculo", __name__)

vehiculo_schema = VehiculoSchema()
vehiculos_schema = VehiculoSchema(many=True)


@ruta_vehiculo.route("/vehiculo", methods=["GET"])
def vehiculo():
    resultall = Vehiculo.query.all()
    resultado_Vehiculo = vehiculos_schema.dump(resultall)
    return jsonify(resultado_Vehiculo)


@ruta_vehiculo.route("/savevehiculo", methods=["POST"])
def save():
    placaVehiculo = request.json["placa"]
    modeloVehiculo = request.json["modelo"]
    estadoVehiculo = request.json["estado"]
    capacidadVehiculo = request.json["capacidad"]
    new_solicitud = Vehiculo(
        placaVehiculo,
        modeloVehiculo,
        estadoVehiculo,
        capacidadVehiculo,
    )
    db.session.add(
        new_solicitud,
    )
    db.session.commit()
    return "Datos guardado con exito"

@ruta_vehiculo.route("/updatevehiculo", methods=["PUT"])
def Update():
    idVehiculo = request.json["id"]
    idPlaca = request.json["placa"]
    modeloVehiculo = request.json["modelo"]
    estadoVehiculo = request.json["estado"]
    capacidadVehiculo = request.json["capacidad"]
    solicitud = Vehiculo.query.get(idVehiculo)
    if solicitud:
        print(solicitud)
        # solicitud.id = idVehiculo
        solicitud.placa = idPlaca
        solicitud.modelo = modeloVehiculo
        solicitud.estado =  estadoVehiculo
        solicitud.capacidad = capacidadVehiculo

        db.session.commit()
        return "Datos actualizados con exitos"
    else:
        return "Error :/ "

@ruta_vehiculo.route("/deletevehiculo/<id>", methods=["DELETE"])
def eliminar(id):
    solicitud = Vehiculo.query.get(id)
    db.session.delete(solicitud)
    db.session.commit()
    return jsonify(
        vehiculo_schema.dump(solicitud),
    )
