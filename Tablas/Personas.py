from sqlalchemy import Column, Integer, String, Date, DateTime, ForeignKey, extract, case, and_
from sqlalchemy.orm import relationship
from sqlalchemy.ext.hybrid import hybrid_property
from Gestores_personas import MixinAsDict, MixinGetByFirstName, MixinGetByLastName
from Configuracion_BD import Base
import datetime

class Personas(Base, MixinAsDict, MixinGetByFirstName, MixinGetByLastName):
	__tablename__ = "personas"
	id = Column(Integer, primary_key = True)
	nombre = Column(String(100))
	apellido = Column(String(100))
	email = Column(String(255), unique = True)
	birthdate = Column(Date)
	personal_id = Column(String(50), unique = True)
	fecha_insercion = Column (DateTime,default=datetime.datetime.now)
	fecha_actualizacion = Column (DateTime)
	estado = Column (String(20), default="A")
	genero_id = Column(Integer,ForeignKey("genero.id"))
	ubicacion_id = Column(Integer, ForeignKey("ubicaciones.id"))
	tipo_id = Column(Integer,ForeignKey("tipo_persona.id"))

	genero = relationship("Genero", backref = "related_genero")
	ubicacion = relationship("Ubicaciones", backref = "related_ubicacion")
	tipo_persona = relationship("Tipo_Persona", backref = "related_tipo_persona")	
	

	@hybrid_property
	def age(self):
		today = datetime.date.today()
		edad = today.year - self.birthdate.year
		if ((today.year, today.month, today.day) < (today.year, self.birthdate.month, self.birthdate.day)):
			edad -= 1
		return edad

	@age.expression
	def age(cls):
		today = datetime.date.today()
		return case (
			[ 
				(and_(datetime.datetime.today().month < extract("month",cls.birthdate), datetime.datetime.today().day < extract("day",cls.birthdate)), today.year - extract("year",cls.birthdate) - 1 )
				], 
			else_=today.year - extract("year",cls.birthdate)
			)