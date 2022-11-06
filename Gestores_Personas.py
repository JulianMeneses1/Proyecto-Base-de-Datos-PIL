from sqlalchemy import Column, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from Configuración_BD import engine


engine.connect() # Conexión a la base de datos
Base = declarative_base()
Session = sessionmaker(bind = engine)
session = Session() # Se abre la sesión

class MixinAsDict:
	def as_dict(self):
		return {c.nombre: getattr(self, c.nombre) for c in self.__table__.columns}

class MixinGetByFirstName: #para buscar por el nombre
	nombre = Column(String(55), unique=True, nullable=True)

	@classmethod
	def get_by_Firstname(cls, nombre):
		session_interna = Session() #se llama session_interna para diferenciarla de la variable global session
		result = session.query(cls).filter(cls.nombre == nombre).first()
		session_interna.close()
		return result

class MixinGetByLastName: #para buscar por el apellido
	apellido = Column(String(55), unique=True, nullable=True)

	@classmethod
	def get_by_Lastname(cls, apellido):
		session_interna = Session() 
		result = session.query(cls).filter(cls.apellido == apellido).first()
		session_interna.close()
		return result



