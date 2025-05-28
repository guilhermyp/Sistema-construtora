from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from core.banco import get_db
from models.Funcionario import Funcionario as FuncionarioModel
from schemas.funcionario import FuncionarioCreate, FuncionarioResponse
from models.Funcionario import Funcionario as FuncionarioModel


router = APIRouter(prefix="/funcionario", tags=["Funcionario"])

@router.post("/")
def criar_funcionario(funcionario: FuncionarioCreate, db: Session = Depends(get_db)):
    db_funcionario = FuncionarioModel(**funcionario.model_dump())
    db.add(db_funcionario)
    db.commit()
    db.refresh(db_funcionario)
    return db_funcionario
