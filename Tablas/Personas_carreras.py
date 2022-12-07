from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship
from Configuracion_BD import Base
import datetime

class Personas_Carreras(Base):
	__tablename__ = "personas_carreras"
	__table_args__ = (UniqueConstraint('persona_id','carrera_id', name="uidx_inscripcion_unica"), )
	id = Column (Integer, primary_key=True)
	fecha_insercion = Column (DateTime,default=datetime.datetime.now)
	fecha_actualizacion = Column (DateTime)
	estado = Column(String(20), default="A")
	persona_id = Column (ForeignKey("personas.id"), nullable=False)
	carrera_id = Column (ForeignKey("carreras.id"), nullable=False)

	persona = relationship("Personas", backref = "related_personas")
	carrera = relationship("Carreras", backref= "related_carreras")