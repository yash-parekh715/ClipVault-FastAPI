import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# DATABASE_URL = os.getenv("DATABASE_URL")
DATABASE_URL = "mysql+pymysql://sql12766426:DPUi2ekX1Y@sql12.freesqldatabase.com:3306/sql12766426"


engine = create_engine(DATABASE_URL, pool_size=10,
                       max_overflow=30, pool_recycle=3600, pool_pre_ping=True,
                       connect_args={
                           "connect_timeout": 10,
                       })

Sessionlocal = sessionmaker(autoflush=False, autocommit=False, bind=engine)

Base = declarative_base()
