from sqlalchemy import Column, Integer, String, DateTime
from Configuracion_BD import Base
import datetime

class Paises(Base):
	__tablename__ = "paises"
	id = Column(Integer, primary_key = True)
	nombre = Column(String(100), unique = True)
	fecha_insercion = Column (DateTime,default=datetime.datetime.now)
	fecha_actualizacion = Column (DateTime)
	estado = Column (String(20), default="A")