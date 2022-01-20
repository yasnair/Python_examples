import sqlalchemy as db
from sqlalchemy import create_engine, Column, Integer, Sequence, String, Date, Float, BIGINT, MetaData
from config import Config

# specify database configurations
db_user = Config.USER_DB
db_pwd  = Config.PASSWORD
db_host = Config.HOST
db_port = Config.PORT
db_name = Config.DATABASE

connection_str = f'mysql+pymysql://{db_user}:{db_pwd}@{db_host}:{db_port}/{db_name}'


# connect to database
print('******* antes de conectar *******')
engine = db.create_engine(connection_str)
connection = engine.connect()

meta = db.MetaData()

print(meta.tables.keys())

for key in meta.tables.keys():
    print(key)

user = db.Table('user', meta, autoload=True, autoload_with=engine) 
print(user.columns.keys())   
