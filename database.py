import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

DATABASE_URL = os.getenv("DATABASE_URL")


engine = create_engine(DATABASE_URL, pool_size=10,
                       max_overflow=30, pool_recycle=3600, pool_pre_ping=True,
                       connect_args={
                           "connect_timeout": 10,
                       })

Sessionlocal = sessionmaker(autoflush=False, autocommit=False, bind=engine)

Base = declarative_base()
