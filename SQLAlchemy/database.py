"""Database engine & session creation."""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import Config

# specify database configurations
db_user = Config.USER_DB
db_pwd  = Config.PASSWORD
db_host = Config.HOST
db_port = Config.PORT
db_name = Config.DATABASE

#db_name = 'mysql'

connection_str = f'mysql+pymysql://{db_user}:{db_pwd}@{db_host}:{db_port}/{db_name}'

engine = create_engine(connection_str)
connection = engine.connect()

Session = sessionmaker(bind=engine)
session = Session()

