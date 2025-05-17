from fastapi import APIRouter, HTTPException
from models import Material
from typing import List

from schemas.material import MaterialCreate, MaterialOut
from services.material import criar_material, listar_materiais
from core.database import SessionLocal

router = APIRouter(prefix="/materiais", tags=["Materiais"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# @router.post("/", response_model=MaterialOut)
# def adicionar_material(material: MaterialCreate, db: Session = Depends(get_db)):
#     return criar_material(db, material)

# @router.get("/", response_model=list[MaterialOut])
# def obter_materiais(db: Session = Depends(get_db)):
#     return listar_materiais(db)


# router = APIRouter()

# @router.post("/", response_model=Material)
# def cadastrar_material(material: Material):
    
#     return material