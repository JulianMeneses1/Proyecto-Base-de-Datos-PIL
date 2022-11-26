from sqlalchemy import func, between
from Tablas import crear_conexion,obtener_sesion,Profesores,Alumnos,Carreras,Profesores_Carreras,Alumnos_Carreras, Facultades,Ramas,Campus,Provincias,Ciudades,Municipios,Paises,Ubicacion,Genero

base_mysql="pil_trabajo_practico"  # nombre de la base de datos

engine_mysql = crear_conexion("mysql","root","Contadores2","127.0.0.1:4000",base_mysql) # Conexión a la base de datos

session_mysql = obtener_sesion(engine_mysql) # abro la sesión en la conexión establecida

# LISTADO CON LA CANTIDAD DE ALUMNOS POR CARRERAS

def alumnosxcarreras():
    resultados=session_mysql.query(Carreras.nombre,func.count(Alumnos_Carreras.carrera_id)).select_from(Alumnos).join(Alumnos_Carreras).join(Carreras).group_by(Carreras.nombre)
    for x in resultados:
        print(f"En la carrera {x[0]} hay inscriptos {x[1]} estudiantes")
        
# alumnosxcarreras()

# LISTADO CON LA CANTIDAD DE PROFESORES POR CARRERAS

def profesoresxcarreras():
    resultados=session_mysql.query(Carreras.nombre,func.count(Profesores_Carreras.carrera_id)).select_from(Profesores).join(Profesores_Carreras).join(Carreras).group_by(Carreras.nombre)
    for x in resultados:
        print(f"En la carrera {x[0]} hay {x[1]} profesores")

# profesoresxcarreras()    

# LISTADO CON EL DETALLE DE LA CANTIDAD DE ALUMNOS POR PROVINCIA DE ORIGEN Y CARRERA QUE CURSAN 

def alumnosxprovincias_carreras():
    resultados=session_mysql.query(Provincias.nombre,Alumnos.nombre,Carreras.nombre).select_from(Alumnos).join(Ubicacion).join(Provincias).join(Alumnos_Carreras).join(Carreras).group_by(Provincias.nombre,Alumnos.nombre).order_by(Provincias.nombre)
    for x in resultados:
        print(f"Provincia: {x[0]}, estudiante: {x[1]}, carrera que cursa: {x[2]}")

# alumnosxprovincias_carreras()

# DISTRIBUCIÓN DE ALUMNOS POR CARRERA Y GRUPO ETARIO (<20 AÑOS, ENTRE 20 AÑOS Y 30 AÑOS, >30 AÑOS) 

def alumnos_carrera_menores_20():

    resultados=session_mysql.query(Carreras.nombre,Alumnos.nombre,Alumnos.edad).select_from(Alumnos).join(Alumnos_Carreras).join(Carreras).group_by(Carreras.nombre,Alumnos.nombre).where(Alumnos.edad<20)
    for x in resultados:
        print(x)

# alumnos_carrera_menores_20()

def alumnos_carrera_entre_20_30():

    resultados=session_mysql.query(Carreras.nombre,Alumnos.nombre,Alumnos.edad).select_from(Alumnos).join(Alumnos_Carreras).join(Carreras).group_by(Carreras.nombre,Alumnos.nombre).where(Alumnos.edad.between(20,30))
    for x in resultados:
        print(x)

# alumnos_carrera_entre_20_30()

def alumnos_carrera_mayores_30():

    resultados=session_mysql.query(Carreras.nombre,Alumnos.nombre,Alumnos.edad).select_from(Alumnos).join(Alumnos_Carreras).join(Carreras).group_by(Carreras.nombre,Alumnos.nombre).where(Alumnos.edad>30)
    for x in resultados:
        print(x)

# alumnos_carrera_mayores_30()

# LISTADO DE PROFESORES RELACIONADO CON CADA ALUMNO

def profesoresxalumnos():

    resultados=session_mysql.query(Profesores.nombre,Alumnos.nombre).select_from(Alumnos).join(Alumnos_Carreras).join(Carreras).join(Profesores_Carreras).join(Profesores).group_by(Profesores.id,Alumnos.id).order_by(Profesores.nombre)
    for x in resultados:
        print(f"Profesor: {x[0]}, Alumno: {x[1]}")

# profesoresxalumnos()



