from sqlalchemy import Column, String
from Configuración_BD import crear_conexion, obtener_sesion

base_mysql="pil_trabajo_practico" # nombre de la base de datos

engine_mysql = crear_conexion("mysql","root","Contadores2","127.0.0.1:4000",base_mysql) # Conexión a la base de datos


session_mysql = obtener_sesion(engine_mysql) # abro la sesión en la conexión establecida

class MixinAsDict:
	def as_dict(self):
		return {c.nombre: getattr(self, c.nombre) for c in self.__table__.columns}

class MixinGetByFirstName: # para buscar por el nombre
	nombre = Column(String(55), unique=True, nullable=True)

	@classmethod
	def get_by_Firstname(cls, nombre):
		session_interna = session_mysql #se llama session_interna para diferenciarla de la variable global session
		result = session_interna.query(cls).filter(cls.nombre == nombre).first()
		session_interna.close()
		return result

class MixinGetByLastName: # para buscar por el apellido
	apellido = Column(String(55), unique=True, nullable=True)

	@classmethod
	def get_by_Lastname(cls, apellido):
		session_interna = session_mysql 
		result = session_interna.query(cls).filter(cls.apellido == apellido).first()
		session_interna.close()
		return result



