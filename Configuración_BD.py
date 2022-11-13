from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database

engine = create_engine('mysql://root:Contadores2@127.0.0.1:4000/pil_trabajo', echo=False) # conexión a la base de datos en mysql

if not database_exists(engine.url):  # Si la base de datos no existe en mysql, entonces se la crea
    create_database(engine.url)







