from flask import request, jsonify, abort
from app import app, db
from models import Solicitud, Grimorio
import random

@app.route('/solicitud/', methods=['POST'])
def crear_solicitud():
    data = request.get_json()
    if not validar_solicitud(data):
        abort(400, description="Datos de solicitud inválidos")
    nueva_solicitud = Solicitud(**data)
    db.session.add(nueva_solicitud)
    db.session.commit()
    return jsonify({"mensaje": "Solicitud creada", "id": nueva_solicitud.id}), 201

@app.route('/solicitud/<int:id>/', methods=['PUT'])
def actualizar_solicitud(id):
    solicitud = Solicitud.query.get_or_404(id)
    data = request.get_json()
    if not validar_solicitud(data):
        abort(400, description="Datos de solicitud inválidos")
    for key, value in data.items():
        setattr(solicitud, key, value)
    db.session.commit()
    return jsonify({"mensaje": "Solicitud actualizada"})

@app.route('/solicitud/<int:id>/estatus/', methods=['PATCH'])
def actualizar_estatus_solicitud(id):
    solicitud = Solicitud.query.get_or_404(id)
    data = request.get_json()
    if 'estatus' not in data:
        abort(400, description="Estatus es requerido")
    solicitud.estatus = data['estatus']
    if solicitud.estatus == "aprobada":
        asignar_grimorio(solicitud)
    db.session.commit()
    return jsonify({"mensaje": "Estatus actualizado"})

@app.route('/solicitudes/', methods=['GET'])
def obtener_solicitudes():
    solicitudes = Solicitud.query.all()
    return jsonify([solicitud.to_dict() for solicitud in solicitudes])

@app.route('/asignaciones/', methods=['GET'])
def obtener_asignaciones():
    asignaciones = Grimorio.query.all()
    return jsonify([asignacion.to_dict() for asignacion in asignaciones])

@app.route('/solicitud/<int:id>/', methods=['DELETE'])
def eliminar_solicitud(id):
    solicitud = Solicitud.query.get_or_404(id)
    db.session.delete(solicitud)
    db.session.commit()
    return jsonify({"mensaje": "Solicitud eliminada"})

def validar_solicitud(data):
    # Implementa validación aquí
    return True

def asignar_grimorio(solicitud):
    tipos_grimorio = ["trébol de una hoja", "trébol de dos hojas", "trébol de tres hojas", "trébol de cuatro hojas", "trébol de cinco hojas"]
    grimorio = Grimorio(tipo=random.choice(tipos_grimorio), estudiante=solicitud)
    db.session.add(grimorio)

if __name__ == "__main__":
    app.run(debug=True)
