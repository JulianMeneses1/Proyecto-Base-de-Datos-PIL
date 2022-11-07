from sqlalchemy import MetaData, Column, Integer, String, Date, DateTime, ForeignKey, extract, case, and_
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.hybrid import hybrid_property
from Gestores_Personas import MixinAsDict, MixinGetByFirstName, MixinGetByLastName
from Configuración_BD import engine
import datetime


engine.connect() # Conexión a la base de datos
Base = declarative_base()
meta = MetaData()
Session = sessionmaker(bind = engine)
session = Session() # Se abre la sesión


class Facultades(Base):    
    __tablename__ = "facultades"

    id = Column (Integer, primary_key=True)
    nombre = Column (String(80))
    fecha_insercion = Column (DateTime,default=datetime.datetime.now)
    fecha_actualizacion = Column (DateTime)
    estado = Column (String(20), default="A")
    carreras = relationship("Carreras",back_populates="facultades")

    def __init__(self, nombre):
        self.nombre = nombre  
 
class Campus(Base):
    __tablename__ = "campus"

    id = Column (Integer, primary_key=True)
    nombre = Column (String(80))
    fecha_insercion = Column (DateTime,default=datetime.datetime.now)
    fecha_actualizacion = Column (DateTime)
    estado = Column (String(20), default="A")
    carreras = relationship ("Carreras",back_populates="campus")

    def __init__(self, nombre):
        self.nombre = nombre

class Ramas(Base):
    __tablename__ = "ramas"

    id = Column (Integer, primary_key=True)
    nombre = Column (String(80))
    fecha_insercion = Column (DateTime,default=datetime.datetime.now)
    fecha_actualizacion = Column (DateTime)
    estado = Column (String(20), default="A")
    carreras = relationship("Carreras",back_populates="ramas")

    def __init__(self, nombre):
        self.nombre = nombre

class Genero(Base):
    __tablename__ = "genero"

    id = Column ('id', Integer, primary_key=True)
    tipo = Column ('tipo', String(30))
    fecha_insercion = Column (DateTime,default=datetime.datetime.now)
    fecha_actualizacion = Column (DateTime)
    estado = Column (String(20), default="A")
    profesores = relationship("Profesores",back_populates="genero")
    alumnos = relationship("Alumnos",back_populates="genero")

    def __init__(self, tipo):
        self.tipo = tipo   
         
        

class Ubicacion(Base):
    __tablename__ = 'ubicacion'

    id = Column (Integer, primary_key=True)
    ciudad = Column (String(50))
    municipio = Column (String(50))
    provincia = Column (String(50))
    fecha_insercion = Column (DateTime,default=datetime.datetime.now)
    fecha_actualizacion = Column (DateTime)
    estado = Column (String(20), default="A")
    alumnos = relationship("Alumnos",back_populates="ubicacion")
    profesores = relationship("Profesores",back_populates="ubicacion")

    def __init__(self, ciudad, municipio, provincia):
        self.ciudad = ciudad
        self.municipio = municipio
        self.provincia = provincia


class Profesores(MixinAsDict,MixinGetByFirstName,MixinGetByLastName,Base):
    __tablename__ = "profesores"

    id = Column (Integer, primary_key=True)
    dni = Column (Integer, unique=True)    
    nombre = Column (String(55))
    apellido = Column (String(55))
    email = Column (String(55))
    pais = Column (String(30))
    fecha_nacimiento = Column (Date)
    fecha_insercion = Column (DateTime,default=datetime.datetime.now)
    fecha_actualizacion = Column (DateTime, nullable=True)
    estado = Column(String(20), default="A")
    ubicacion_id = Column (ForeignKey("ubicacion.id"))    
    genero_id = Column (ForeignKey("genero.id"))
    genero = relationship("Genero", back_populates= "profesores")
    ubicacion = relationship("Ubicacion", back_populates= "profesores")
    carreras = relationship("Carreras", secondary= "profesores_carreras", back_populates="profesores")   
    

    def __init__(self, dni, nombre, apellido, email, pais, fecha_nacimiento, ubicacion_id, genero_id):
        self.dni = dni
        self.nombre = nombre    
        self.apellido = apellido
        self.email = email
        self.pais = pais
        self.fecha_nacimiento = fecha_nacimiento
        self.ubicacion_id = ubicacion_id
        self.genero_id = genero_id

    @hybrid_property
    def nombrecompleto(self):
        if self.nombre is not None:
            return self.nombre + " " + self.apellido
        else:
            return self.apellido

    @nombrecompleto.expression
    def nombrecompleto(cls):
        return case(
			[(cls.nombre != None, cls.nombre + " " + cls.apellido),], 
			else_ = cls.apellido
			)

    @hybrid_property
    def edad(self):
        today = datetime.date.today()
        edad = today.year - self.fecha_nacimiento.year
        if ((today.year, today.month, today.day) < (today.year, self.fecha_nacimiento.month, self.fecha_nacimiento.day)):
            edad -= 1
        return edad
	
    @edad.expression
    def edad(cls):
        today = datetime.date.today()
        return case (
			[ 
				(and_(datetime.datetime.today().month < extract("month",cls.fecha_nacimiento), datetime.datetime.today().day < extract("day",cls.fecha_nacimiento)), today.year - extract("year",cls.fecha_nacimiento) - 1 )
				],  #and_ sería el equivalente de and en python
			else_=today.year - extract("year",cls.fecha_nacimiento) #else_ equivalente de else en python
			)
		
    

class Alumnos(MixinAsDict,MixinGetByFirstName,MixinGetByLastName,Base):
    __tablename__ = "alumnos"

    id = Column (Integer, primary_key=True)
    dni = Column (Integer, unique=True)    
    nombre = Column (String(55))
    apellido = Column (String(55))
    email = Column (String(55))
    pais = Column (String(30))
    fecha_nacimiento = Column (Date)
    fecha_insercion = Column (DateTime,default=datetime.datetime.now)
    fecha_actualizacion = Column (DateTime)
    estado = Column(String(20), default="A")
    ubicacion_id = Column (ForeignKey("ubicacion.id"))
    genero_id = Column (ForeignKey("genero.id"))
    genero = relationship("Genero", back_populates= "alumnos")
    ubicacion = relationship("Ubicacion", back_populates= "alumnos")
    carreras = relationship("Carreras", secondary= "alumnos_carreras", back_populates="alumnos")

    def __init__(self, dni, nombre, apellido, email, pais, fecha_nacimiento, ubicacion_id, genero_id):
        self.dni = dni
        self.nombre = nombre    
        self.apellido = apellido
        self.email = email
        self.pais = pais
        self.fecha_nacimiento = fecha_nacimiento
        self.ubicacion_id = ubicacion_id
        self.genero_id = genero_id

    @hybrid_property
    def nombrecompleto(self):
        if self.nombre is not None:
            return self.nombre + " " + self.apellido
        else:
            return self.apellido

    @nombrecompleto.expression
    def nombrecompleto(cls):
        return case(
			[(cls.nombre != None, cls.nombre + " " + cls.apellido),], 
			else_ = cls.apellido
			)

    @hybrid_property
    def edad(self):
        today = datetime.date.today()
        edad = today.year - self.fecha_nacimiento.year
        if ((today.year, today.month, today.day) < (today.year, self.fecha_nacimiento.month, self.fecha_nacimiento.day)):
            edad -= 1
        return edad
	
    @edad.expression
    def edad(cls):
        today = datetime.date.today()
        return case (
			[ 
				(and_(datetime.datetime.today().month < extract("month",cls.fecha_nacimiento), datetime.datetime.today().day < extract("day",cls.fecha_nacimiento)), today.year - extract("year",cls.fecha_nacimiento) - 1 )
				],  #and_ sería el equivalente de and en python
			else_=today.year - extract("year",cls.fecha_nacimiento) #else_ equivalente de else en python
			)

class Carreras(Base):
    __tablename__ = "carreras"

    id = Column (Integer, primary_key=True)
    nombre = Column (String(80))
    fecha_nacimiento = Column (Date)
    fecha_insercion = Column (DateTime,default=datetime.datetime.now)
    fecha_actualizacion = Column (DateTime)
    estado = Column(String(20), default="A")
    ramas_id = Column (ForeignKey("ramas.id"))
    facultades_id = Column (ForeignKey("facultades.id"))
    campus_id = Column (ForeignKey("campus.id"))
    ramas = relationship("Ramas",back_populates="carreras")
    facultades = relationship("Facultades",back_populates="carreras")
    campus = relationship("Campus",back_populates="carreras")
    profesores = relationship("Profesores", secondary="profesores_carreras",back_populates="carreras")
    alumnos = relationship("Alumnos", secondary= "alumnos_carreras", back_populates="carreras")  

    def __init__(self, nombre, ramas_id, facultades_id, campus_id):
        self.nombre = nombre
        self.ramas_id = ramas_id
        self.facultades_id = facultades_id
        self.campus_id = campus_id  


class Profesores_Carreras(Base):
    __tablename__ = "profesores_carreras"

    id = Column (Integer, primary_key=True)
    fecha_insercion = Column (DateTime,default=datetime.datetime.now)
    fecha_actualizacion = Column (DateTime)
    estado = Column(String(20), default="A")
    profesor_id = Column (ForeignKey("profesores.id"), nullable=False)
    carrera_id = Column (ForeignKey("carreras.id"), nullable=False)

    def __init__(self, profesor_id, carrera_id):
        self.profesor_id = profesor_id
        self.carrera_id = carrera_id   


class Alumnos_Carreras(Base):
    __tablename__ = "alumnos_carreras"

    id = Column (Integer, primary_key=True)
    fecha_insercion = Column (DateTime,default=datetime.datetime.now)
    fecha_actualizacion = Column (DateTime)
    estado = Column(String(20), default="A")
    alumno_id = Column (ForeignKey("alumnos.id"), nullable=False)
    carrera_id = Column (ForeignKey("carreras.id"), nullable=False)

    def __init__(self, alumno_id, carrera_id):
        self.alumno_id = alumno_id
        self.carrera_id = carrera_id  


Base.metadata.create_all(engine) #creación de las tablas





