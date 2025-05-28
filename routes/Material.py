from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models.Material import Material
from typing import List
from core.banco import get_db
from schemas.material import MaterialCreate,MaterialResponse, MaterialUpdate
from services.estoque import criar_material, listar_materiais
from core.banco import Base, SessionLocal
from models.Material import Material as MaterialModel

router = APIRouter(prefix="/materiais", tags=["Materiais"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/")
def criar_material(material: MaterialCreate, db: Session = Depends(get_db)):
    db_material = MaterialModel(**material.model_dump())
    db.add(db_material)
    db.commit()
    db.refresh(db_material)
    return db_material

