from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

DATABASE_URL="mysql+pymysql://admin:adminadmin@do-epic-shit.cf3alghuei5c.ap-south-1.rds.amazonaws.com:3306/StudentDetails"    

engine = create_engine(DATABASE_URL, pool_size=10, max_overflow=30)

Sessionlocal = sessionmaker(autoflush=False, autocommit=False, bind=engine)

Base = declarative_base()