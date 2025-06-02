from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from core.banco import get_db
from models.funcionario import Funcionario as FuncionarioModel
from schemas.funcionario import FuncionarioCreate, FuncionarioResponse, FuncionarioUpdate
from services import funcionario_service


router = APIRouter(prefix="/funcionario", tags=["Funcionario"])

@router.post("/", response_model=FuncionarioResponse)
def criar(funcionario: FuncionarioCreate, db: Session = Depends(get_db)):
    return funcionario_service.criar_funcionario(db, funcionario)

@router.get("/", response_model=list[FuncionarioResponse])
def listar(db: Session = Depends(get_db)):
    return funcionario_service.listar_funcionarios(db)


@router.get("/{funcionario_id}", response_model=FuncionarioResponse)
def buscar(funcionario_id: int, db: Session = Depends(get_db)):
    funcionario = funcionario_service.buscar_funcionario(db, funcionario_id)
    if not funcionario:
        raise HTTPException(status_code=404, detail="Funcionário não encontrado")
    return funcionario


@router.put("/{funcionario_id}", response_model=FuncionarioResponse)
def atualizar(funcionario_id: int, dados: FuncionarioUpdate, db: Session = Depends(get_db)):
    funcionario = funcionario_service.atualizar_funcionario(db, funcionario_id, dados)
    if not funcionario:
        raise HTTPException(status_code=404, detail="Funcionário não encontrado")
    return funcionario


@router.delete("/{funcionario_id}")
def deletar(funcionario_id: int, db: Session = Depends(get_db)):
    funcionario = funcionario_service.deletar_funcionario(db, funcionario_id)
    if not funcionario:
        raise HTTPException(status_code=404, detail="Funcionário não encontrado")
    return {"ok": True, "mensagem": "Funcionário excluído com sucesso"}