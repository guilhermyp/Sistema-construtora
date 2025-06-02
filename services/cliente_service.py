from sqlalchemy.orm import Session
from models.cliente import Cliente
from schemas.cliente import ClienteCreate, ClienteUpdate
from models.projeto import Projeto
from fastapi import HTTPException


def criar_cliente(db: Session, cliente: ClienteCreate):
    if cliente.projeto_id is not None:
        projeto = db.query(Projeto).filter(Projeto.id == cliente.projeto_id).first()
        if not projeto:
            raise HTTPException(status_code=404, detail="ID do projeto não encontrado")

    novo_cliente = Cliente(**cliente.dict())
    db.add(novo_cliente)
    db.commit()
    db.refresh(novo_cliente)
    return novo_cliente


def listar_clientes(db: Session):
    return db.query(Cliente).all()


def buscar_cliente(db: Session, cliente_id: int):
    return db.query(Cliente).filter(Cliente.id == cliente_id).first()


def atualizar_cliente(db: Session, cliente_id: int, dados: ClienteUpdate):
    cliente = db.query(Cliente).filter(Cliente.id == cliente_id).first()
    if not cliente:
        return None

    if dados.projeto_id is not None:
        projeto = db.query(Projeto).filter(Projeto.id == dados.projeto_id).first()
        if not projeto:
            raise HTTPException(status_code=404, detail="ID do projeto não encontrado")

    for campo, valor in dados.dict(exclude_unset=True).items():
        setattr(cliente, campo, valor)

    db.commit()
    db.refresh(cliente)
    return cliente


def deletar_cliente(db: Session, cliente_id: int):
    cliente = db.query(Cliente).filter(Cliente.id == cliente_id).first()
    if cliente:
        db.delete(cliente)
        db.commit()
    return cliente
