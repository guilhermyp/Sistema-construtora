from sqlalchemy.orm import Session
from fastapi import HTTPException
from models.projeto import Projeto
from models.funcionario import Funcionario
from schemas.funcionario import FuncionarioCreate, FuncionarioUpdate


def criar_funcionario(db: Session, funcionario: FuncionarioCreate):
    # Verifica se o projeto existe, se informado
    if funcionario.projeto_id is not None:
        projeto = db.query(Projeto).filter(Projeto.id == funcionario.projeto_id).first()
        if not projeto:
            raise HTTPException(status_code=404, detail="O projeto não existe")

    novo_funcionario = Funcionario(**funcionario.dict())
    db.add(novo_funcionario)
    db.commit()
    db.refresh(novo_funcionario)
    return novo_funcionario

def listar_funcionarios(db: Session):
    return db.query(Funcionario).all()


def buscar_funcionario(db: Session, funcionario_id: int):
    return db.query(Funcionario).filter(Funcionario.id == funcionario_id).first()


def atualizar_funcionario(db: Session, funcionario_id: int, dados: FuncionarioUpdate):
    funcionario = db.query(Funcionario).filter(Funcionario.id == funcionario_id).first()
    if not funcionario:
        return None

    if dados.projeto_id is not None:
        projeto = db.query(Projeto).filter(Projeto.id == dados.projeto_id).first()
        if not projeto:
            raise HTTPException(status_code=404, detail="O projeto não existe")

    for campo, valor in dados.dict(exclude_unset=True).items():
        setattr(funcionario, campo, valor)

    db.commit()
    db.refresh(funcionario)
    return funcionario


def deletar_funcionario(db: Session, funcionario_id: int):
    funcionario = db.query(Funcionario).filter(Funcionario.id == funcionario_id).first()
    if funcionario:
        db.delete(funcionario)
        db.commit()
    return funcionario
