from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

def crear_conexion(db_connector,db_user, db_password, db_ip_address ,db_name): # Función para generar las conexiones a los diferentes motores de bases de datos,
																				# los parámetros son el conector, el usuario, la contraseña, la dirección ip y el nombre de la base de datos
	url = f"{db_connector}://{db_user}:{db_password}@{db_ip_address}/{db_name}" # esta es la conexión
	try:
		engine = create_engine(url, echo = False)
		if not database_exists(engine.url):    # Si la base de datos no existe, entonces se la crea
			create_database(engine.url)
		else:
			pass
		return engine  # la función devuelve como valor la conexión
	except:
		print(f"Error al crear conector {db_connector}, servidor: {db_ip_address}")
		return None

def obtener_sesion(engine): # función para abrir la sesión de la conexión que se elija
	Session = sessionmaker(bind = engine)
	return Session()