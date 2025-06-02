from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from core.banco import get_db
from schemas.material import MaterialCreate,MaterialResponse, MaterialUpdate
from services.estoque import criar_material, listar_materiais, buscar_material, atualizar_material, deletar_material
from core.banco import SessionLocal
from models.material import Material as MaterialModel
from models.projeto import Projeto as ProjetoModel


router = APIRouter(prefix="/materiais", tags=["Materiais"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/")
def criar_material(material: MaterialCreate, db: Session = Depends(get_db)):
    if material.projeto_id is not None:
        projeto = db.query(ProjetoModel).filter(ProjetoModel.id == material.projeto_id).first()
        if not projeto:
            raise HTTPException(status_code=404, detail="Projeto não encontrado")
    db_material = MaterialModel(**material.model_dump())
    db.add(db_material)
    db.commit()
    db.refresh(db_material)
    return db_material

@router.get("/", response_model=List[MaterialResponse]) 
def listar(db: Session = Depends(get_db)):
    return listar_materiais(db=db)

@router.get("/{material_id}", response_model=MaterialResponse)
def buscar(material_id: int, db: Session = Depends(get_db)):
    material = buscar_material(db, material_id)
    if material is None:
        raise HTTPException(status_code=404, detail="Material não encontrado")
    return material


@router.put("/{material_id}", response_model=MaterialResponse)
def atualizar(material_id: int, material_data: MaterialUpdate, db: Session = Depends(get_db)):
    # Se projeto_id for informado, verifica se existe
    if material_data.projeto_id is not None:
        projeto = db.query(ProjetoModel).filter(ProjetoModel.id == material_data.projeto_id).first()
        if not projeto:
            raise HTTPException(status_code=404, detail="Projeto não encontrado")

    updated_material = atualizar_material(db, material_id, material_data)
    if updated_material is None:
        raise HTTPException(status_code=404, detail="Material não encontrado")
    return updated_material

@router.delete("/{material_id}", status_code=200)
def deletar(material_id: int, db: Session = Depends(get_db)):
    deleted_material = deletar_material(db, material_id)
    if deleted_material is None:
        raise HTTPException(status_code=404, detail="Material não encontrado")
    return {"ok": "Material deletado com sucesso"}