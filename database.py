from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

DATABASE_URL = "127.0.0.1:3306"

engine = create_engine(DATABASE_URL, pool_size=10, max_overflow=30)

Sessionlocal = sessionmaker(autoflush=False, autocommit=False, bind=engine)

Base = declarative_base()
