from sqlalchemy import Column, Integer, String, Float
from app.database import Base

class RevenuDB(Base):
    __tablename__ = "revenus"
    id = Column(Integer, primary_key=True, index=True)
    montant = Column(Float)
    description = Column(String)

class DepenseDB(Base):
    __tablename__ = "depenses"
    id = Column(Integer, primary_key=True, index=True)
    montant = Column(Float)
    description = Column(String)
    categorie = Column(String)
