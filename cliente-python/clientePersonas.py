import sys
import datetime
import configparser
import requests
from requests.structures import CaseInsensitiveDict
import datetime
from datetime import timedelta


#Variables globales para verificacion
api_personas_url_base = None
archivo_config = 'ConfigFile.properties'

def cargar_variables():
    config = configparser.RawConfigParser()
    config.read(archivo_config)

    global api_personas_url_base
    api_personas_url_base = config.get('SeccionApi', 'api_personas_url_base')


def listar():
    headers = CaseInsensitiveDict()
    headers["Accept"] = "application/json"
    headers["Content-Type"] = "application/json"

    datos = { }
    
    url_listar = api_personas_url_base
    
    r = requests.get(url_listar, headers=headers, json=datos)
    if (r.status_code == 200):
        # Validar response
        listado = r.json()
        for item in listado:
            print( "      " + str(item) )
    else:
        print( "Error " + str(r.status_code))


def crear(cedula: int, nombre: str, apellido: str):
    headers = CaseInsensitiveDict()
    headers["Accept"] = "application/json"
    headers["Content-Type"] = "application/json"

    datos = {'cedula': cedula, 
             'nombre' : nombre,
             'apellido' : apellido
            }
    
    url_crear = api_personas_url_base 
    
    r = requests.post(url_crear, headers=headers, json=datos)
    if (r.status_code >= 200 and r.status_code < 300):
        # Validar response
        print(r)
        
    else:
        print( "Error " + str(r.status_code))
        print(str(r.json()))


#######################################################
######  Procesamiento principal
#######################################################
print("Iniciando " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
cargar_variables()

print("Listar personas:")
listar()
print("________________")


print("Crear persona:")
crear(1000,"Romina", "Lopez")
print("________________")


print("Crear persona:")
crear(1001,"Carlos", "Caballero")
print("________________")


print("Listar personas:")
listar()
print("________________")


print("Finalizando " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))