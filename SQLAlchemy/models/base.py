"""Database engine & session creation."""
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '.')))

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
#from config import Config

'''
# specify database configurations
db_user = Config.USER_DB
db_pwd  = Config.PASSWORD
db_host = Config.HOST
db_port = Config.PORT
db_name = Config.DATABASE

connection_str = f'mysql+pymysql://{db_user}:{db_pwd}@{db_host}:{db_port}/{db_name}'

engine = create_engine(connection_str)
connection = engine.connect()

Session = sessionmaker(bind=engine)
session = Session()

'''

Base = declarative_base()

