from sqlalchemy import Column, Integer, String, String
from database import Base


class Clip(Base):
    __tablename__ = "project"

    ## Columns Name and its Types (Including Indexes Primary Key)

    id = Column(String(20), primary_key=True, index=True)
    data = Column(String(1000))
