from sqlalchemy.orm import sessionmaker
from sqlalchemy import func, between
from Configuración_BD import engine
from Tablas import Profesores,Alumnos,Carreras,Profesores_Carreras,Alumnos_Carreras, Facultades,Ramas,Campus,Provincias,Ciudades,Municipios,Ubicacion,Genero

db=engine.connect()

Session = sessionmaker(bind = engine)
session =  Session()

#  LISTADO CON LA CANTIDAD DE ALUMNOS POR CARRERAS

def alumnosxcarreras():
    resultados=session.query(Carreras.nombre,func.count(Alumnos_Carreras.carrera_id)).select_from(Alumnos).join(Alumnos_Carreras).join(Carreras).group_by(Carreras.nombre)
    for x in resultados:
        print(f"En la carrera {x[0]} hay inscriptos {x[1]} estudiantes")
        
# alumnosxcarreras()

# LISTADO CON LA CANTIDAD DE PROFESORES POR CARRERAS

def profesoresxcarreras():
    resultados=session.query(Carreras.nombre,func.count(Profesores_Carreras.carrera_id)).select_from(Profesores).join(Profesores_Carreras).join(Carreras).group_by(Carreras.nombre)
    for x in resultados:
        print(f"En la carrera {x[0]} hay {x[1]} profesores")

# profesoresxcarreras()

# LISTADO CON EL DETALLE DE LA CANTIDAD DE ALUMNOS POR PROVINCIA DE ORIGEN Y CARRERA QUE CURSAN 

def alumnosxprovincias_carreras():
    resultados=session.query(Provincias.nombre,Alumnos.nombre,Carreras.nombre).select_from(Alumnos).join(Ubicacion).join(Provincias).join(Alumnos_Carreras).join(Carreras).group_by(Provincias.nombre,Alumnos.nombre).order_by(Provincias.nombre)
    for x in resultados:
        print(f"Provincia: {x[0]}, estudiante: {x[1]}, carrera que cursa: {x[2]}")

# alumnosxprovincias_carreras()

# DISTRIBUCIÓN DE ALUMNOS POR CARRERA Y GRUPO ETARIO (<20 AÑOS, ENTRE 20 AÑOS Y 30 AÑOS, >30 AÑOS) 

def alumnos_carrera_menores_20():

    resultados=session.query(Carreras.nombre,Alumnos.nombre,Alumnos.edad).select_from(Alumnos).join(Alumnos_Carreras).join(Carreras).group_by(Carreras.nombre,Alumnos.nombre).where(Alumnos.edad<20)
    for x in resultados:
        print(x)

# alumnos_carrera_menores_20()

def alumnos_carrera_entre_20_30():

    resultados=session.query(Carreras.nombre,Alumnos.nombre,Alumnos.edad).select_from(Alumnos).join(Alumnos_Carreras).join(Carreras).group_by(Carreras.nombre,Alumnos.nombre).where(Alumnos.edad.between(20,30))
    for x in resultados:
        print(x)

# alumnos_carrera_entre_20_30()

def alumnos_carrera_mayores_30():

    resultados=session.query(Carreras.nombre,Alumnos.nombre,Alumnos.edad).select_from(Alumnos).join(Alumnos_Carreras).join(Carreras).group_by(Carreras.nombre,Alumnos.nombre).where(Alumnos.edad>30)
    for x in resultados:
        print(x)

# alumnos_carrera_mayores_30()

# LISTADO DE PROFESORES RELACIONADO CON CADA ALUMNO

def profesoresxalumnos():

    resultados=session.query(Profesores.nombre,Alumnos.nombre).select_from(Alumnos).join(Alumnos_Carreras).join(Carreras).join(Profesores_Carreras).join(Profesores).group_by(Profesores.id,Alumnos.id).order_by(Profesores.nombre)
    for x in resultados:
        print(f"Profesor: {x[0]}, Alumno: {x[1]}")

# profesoresxalumnos()
