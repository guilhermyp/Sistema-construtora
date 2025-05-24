from fastapi import APIRouter, Depends, Session, HTTPException
from models.material import Material
from typing import List

from schemas.material import MaterialCreate, MaterialOut
from services import estoque
from services.estoque import criar_material, listar_materiais
from core.banco import SessionLocal

router = APIRouter(prefix="/materiais", tags=["Materiais"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=MaterialOut)
def adicionar_material(material: MaterialCreate, db: Session = Depends(get_db)):
     return criar_material(db, material)

@router.get("/", response_model=list[MaterialOut])
def obter_materiais(db: Session = Depends(get_db)):
        return listar_materiais(db)


router = APIRouter()

@router.post("/", response_model=Material)
def cadastrar_material(material: Material):    
     return estoque.cadastrar_material(material)
@router.get("/", response_model=List[Material])
def listar_material():
    return estoque.listar_material()