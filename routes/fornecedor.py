from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session
from core.banco import get_db  
from models.Fornecedor import Fornecedor as FornecedorModel
from schemas.fornecedor import FornecedorCreate, FornecedorResponse

router = APIRouter(prefix="/fornecedores", tags=["Fornecedores"])

@router.post("/")
def criar_fornecedor(fornecedor: FornecedorCreate, db: Session = Depends(get_db)):
    db_forn = FornecedorModel(**fornecedor.model_dump())
    db.add(db_forn)
    db.commit()
    db.refresh(db_forn)
    return db_forn