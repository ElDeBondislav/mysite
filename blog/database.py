from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DB_NAME = 'd31m7u11hgkmuf'
engine = create_engine(
    f'postgresql://cmfgxrmblmyxsa:781f734d9640360304e202ba54b870ce7514e1d6c167ba6b998f0f4ab18c5afe@ec2-3-225-110-188.compute-1.amazonaws.com:5432/d31m7u11hgkmuf')

Base = declarative_base()
Base.metadata.create_all(bind=engine)

meta = MetaData()

allowedContainer = Table(
   'allowedusers_v1', meta,
    Column('id', Integer, primary_key=True),
    Column('data', String),
)
instaContainer = Table(
   'instaContainer_v1', meta,
    Column('id', Integer, primary_key=True),
    Column('data', String),
)

meta.create_all(engine)

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()
