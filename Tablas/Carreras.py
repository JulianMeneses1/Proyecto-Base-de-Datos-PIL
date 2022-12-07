from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship
from Configuracion_BD import Base
import datetime

class Carreras(Base):
	__tablename__ = "carreras"
	__table_args__ = (UniqueConstraint('programa_id', 'facultad_id', 'rama_id','campus_id', name='uidx_carrera_unica'),)
	id = Column(Integer, primary_key = True)
	fecha_insercion = Column (DateTime,default=datetime.datetime.now)
	fecha_actualizacion = Column (DateTime)
	estado = Column (String(20), default="A")
	programa_id = Column(Integer, ForeignKey("programas.id"))
	facultad_id = Column(Integer, ForeignKey("facultades.id"))
	rama_id = Column(Integer, ForeignKey("ramas.id"))
	campus_id = Column(Integer, ForeignKey("campus.id"))	

	programa = relationship("Programas", backref = "related_programa")
	facultad = relationship("Facultades", backref = "related_facultad")
	rama = relationship("Ramas", backref = "related_rama")
	campus = relationship("Campus", backref = "related_campus")