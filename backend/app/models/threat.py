from sqlalchemy import Column, Integer, String
from app.database.db import Base

class Threat(Base):

    __tablename__ = "threats"

    id = Column(Integer, primary_key=True)

    severity = Column(String)

    source = Column(String)

    description = Column(String)
