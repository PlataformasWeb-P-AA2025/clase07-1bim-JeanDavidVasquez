from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_ # se importa el operador and

# se importa la clase(s) del
# archivo genera_tablas
from genera_tablas import *

# se importa información del archivo configuracion
from configuracion import cadena_base_datos
# se genera enlace al gestor de base de
# datos
# para el ejemplo se usa la base de datos
# sqlite
engine = create_engine(cadena_base_datos)


Session = sessionmaker(bind=engine)
session = Session()

# Obtener todos los registros de
# la entidad estudiante (clase Estudiante)

estudiantes = session.query(Estudiante).all()
#print(estudiantes)
for est in estudiantes:
    print(f"ID: {est.id}, Apellido: {est.apellido}")

# print("--------------------------------------")
# Obtener todos los registros de la clase Modulo
# modulos = session.query(Modulo).all()
# print(modulos)

print("--------------------------------------")
# Obtener todos los registros de la clase Matricula
#en esta consulta estoy sacandao los estudiantes de cada matricula estoy accediendo a la clase matricula para poder extraes la inforamcion de cada estudiante.
matriculas = session.query(Matricula).all()
for m in matriculas:
    print(f"Estudiante: {m.estudiante.nombre} {m.estudiante.apellido}")

# nombre y apellido del estudiante de cada matrícula

# print(matriculas)
