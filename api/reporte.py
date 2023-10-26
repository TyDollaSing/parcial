from flask import Blueprint, request, jsonify, json
from config.db import db, app, ma
from models.reporte import Reporte, ReporteSchema

ruta_reporte = Blueprint("ruta_reporte", __name__)

reporte_schema = ReporteSchema()
reportes_schema = ReporteSchema(many=True)


@ruta_reporte.route("/reporte", methods=["GET"])
def reporte():
    resultall = Reporte.query.all()
    resultado_reporte = reportes_schema.dump(resultall)
    return jsonify(resultado_reporte)


@ruta_reporte.route("/savereporte", methods=["POST"])
def save():
    tipoReporte = request.json["tipo"]
    fechaGeneracion = request.json["fecha"]
    estado = request.json["estado"]
    contenido = request.json["contenido"]

    new_reporte = Reporte(
        tipoReporte,
        fechaGeneracion,
        estado,
        contenido,
    )
    db.session.add(
        new_reporte,
    )
    db.session.commit()
    return "Datos guardados con exito"



@ruta_reporte.route("/updatereporte", methods=["PUT"])
def Update():
    idReporte = request.json["id"]
    nombre = request.json["tipo_reporte"]
    apellido = request.json["fecha_generacion"]
    email = request.json["estado"]
    tel = request.json["contenido_reporte"]
    reporte = Reporte.query.get(idReporte)
    if reporte:
        print(reporte)
        reporte.tipo_reporte = nombre
        reporte.fecha_generacion = apellido
        reporte.estado = email
        reporte.contenido_reporte = tel
        db.session.commit()
        return "Datos actualizados con exitos"
    else:
        return "Error :/ "

@ruta_reporte.route("/deletereporte/<id>", methods=["DELETE"])
def eliminar(id):
    reporte = Reporte.query.get(id)
    db.session.delete(reporte)
    db.session.commit()
    return jsonify(
        reporte_schema.dump(reporte),
    )
