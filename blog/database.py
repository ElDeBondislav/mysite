from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DB_NAME = 'd31m7u11hgkmuf'
engine = create_engine(
    f'postgresql://zazljrejhlbwrz:dd90bd26aa69487f003fed1b3be1b00d555887eaa9d933c0615ca90b5ba83ed0@ec2-34-225-159-178.compute-1.amazonaws.com:5432/d7lgldjjvkkmfn')

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
