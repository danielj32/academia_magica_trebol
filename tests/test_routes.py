import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_obtener_solicitudes(client):
    response = client.get('/solicitudes/')
    assert response.status_code == 200
    # Aquí puedes agregar más aserciones para verificar el contenido de la respuesta, por ejemplo:
    # assert b"Juan" in response.data

"""Estos test prueban que la informacion es correcta"""
def test_crear_solicitud(client):
    data = {
        "nombre": "Carlos",
        "apellido": "Perez",
        "identificacion": "1244348",
        "edad": 27,
        "afinidad_magica": "fuego"
    }
    response = client.post('/solicitud/', json=data)
    assert response.status_code == 201

def test_crear_solicitud(client):
    data = {
        "nombre": "luis miguel",
        "apellido": "LLeras",
        "identificacion": "124434",
        "edad": 76,
        "afinidad_magica": "tierra"
    }
    response = client.post('/solicitud/', json=data)
    assert response.status_code == 201

def test_crear_solicitud(client):
    data = {
        "nombre": "Valentina",
        "apellido": "Camargo",
        "identificacion": "124428",
        "edad": 28,
        "afinidad_magica": "Oscuridad"
    }
    response = client.post('/solicitud/', json=data)
    assert response.status_code == 201

def test_crear_solicitud(client):
    data = {
        "nombre": "Angelica",
        "apellido": "Ortiz",
        "identificacion": "124459",
        "edad": 28,
        "afinidad_magica": "Viento"
    }
    response = client.post('/solicitud/', json=data)
    assert response.status_code == 201

def test_crear_solicitud(client):
    data = {
        "nombre": "Luisa",
        "apellido": "Milan",
        "identificacion": "1244678",
        "edad": 32,
        "afinidad_magica": "Agua"
    }
    response = client.post('/solicitud/', json=data)
    assert response.status_code == 201

# estos test prueban con informacion erronea la aplicacion no los debe recibir

"""Prueba que la identificacion es demasiado larga"""
"""def test_crear_solicitud(client):
    data = {
        "nombre": "Carlos",
        "apellido": "Perez",
        "identificacion": "1244348222333",
        "edad": 27,
        "afinidad_magica": "fuego"
    }
    response = client.post('/solicitud/', json=data)
    assert response.status_code == 201"""

"""Prueba que la afiniadad magica no es la correcta"""
"""def test_crear_solicitud(client):
    data = {
        "nombre": "Carlos",
        "apellido": "Perez",
        "identificacion": "1244348222333",
        "edad": 27,
        "afinidad_magica": "sal"
    }
    response = client.post('/solicitud/', json=data)
    assert response.status_code == 201"""

"""Prueba que la identifiaacion tiene letras"""
"""def test_crear_solicitud(client):
    data = {
        "nombre": "Carlos",
        "apellido": "Perez",
        "identificacion": "1244348222333",
        "edad": 27er,
        "afinidad_magica": "sal"
    }
    response = client.post('/solicitud/', json=data)
    assert response.status_code == 201"""
