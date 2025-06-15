from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal, Base, engine
from app.models import RevenuDB, DepenseDB
from pydantic import BaseModel
from typing import List

router = APIRouter()

Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class Revenu(BaseModel):
    montant: float
    description: str

class Depense(BaseModel):
    montant: float
    description: str
    categorie: str

@router.post("/revenus")
def create_revenu(revenu: Revenu, db: Session = Depends(get_db)):
    db_revenu = RevenuDB(**revenu.dict())
    db.add(db_revenu)
    db.commit()
    db.refresh(db_revenu)
    return db_revenu

@router.post("/depenses")
def create_depense(depense: Depense, db: Session = Depends(get_db)):
    db_depense = DepenseDB(**depense.dict())
    db.add(db_depense)
    db.commit()
    db.refresh(db_depense)
    return db_depense

@router.get("/solde")
def get_solde(db: Session = Depends(get_db)):
    total_revenus = db.query(RevenuDB).all()
    total_depenses = db.query(DepenseDB).all()

    sum_revenus = sum([r.montant for r in total_revenus])
    sum_depenses = sum([d.montant for d in total_depenses])

    return {"solde": sum_revenus - sum_depenses}
