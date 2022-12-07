from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship
from Configuracion_BD import Base
import datetime

class Ubicaciones(Base):
	__tablename__ = "ubicaciones"
	__table_args__ = (UniqueConstraint('pais_id','ciudad_id','municipio_id','provincia_id', name='uidx_sitio_unico'), )
	id = Column(Integer, primary_key = True)
	fecha_insercion = Column (DateTime,default=datetime.datetime.now)
	fecha_actualizacion = Column (DateTime)
	estado = Column (String(20), default="A")
	pais_id = Column(Integer, ForeignKey("paises.id"))
	ciudad_id = Column(Integer,ForeignKey("ciudades.id"))
	municipio_id = Column(Integer,ForeignKey("municipios.id"))
	provincia_id = Column(Integer,ForeignKey("provincias.id"))

	pais = relationship("Paises", backref = "related_pais")
	ciudad = relationship("Ciudades", backref = "related_ciudad")
	municipio = relationship("Municipios", backref = "related_municipio")
	provincia = relationship("Provincias", backref = "related_provincia")