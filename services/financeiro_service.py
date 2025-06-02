from sqlalchemy.orm import Session
from models.financeiro import Financeiro
from schemas.financeiro import FinanceiroCreate, FinanceiroUpdate

def criar_lancamento(db: Session, dados: FinanceiroCreate):
    novo = Financeiro(**dados.dict())
    db.add(novo)
    db.commit()
    db.refresh(novo)
    return novo

def listar_lancamentos(db: Session):
    return db.query(Financeiro).all()

def buscar_lancamento(db: Session, lancamento_id: int):
    return db.query(Financeiro).filter(Financeiro.id == lancamento_id).first()

def atualizar_lancamento(db: Session, lancamento_id: int, dados: FinanceiroUpdate):
    lancamento = buscar_lancamento(db, lancamento_id)
    if lancamento:
        for campo, valor in dados.dict(exclude_unset=True).items():
            setattr(lancamento, campo, valor)
        db.commit()
        db.refresh(lancamento)
    return lancamento

def deletar_lancamento(db: Session, lancamento_id: int):
    lancamento = buscar_lancamento(db, lancamento_id)
    if lancamento:
        db.delete(lancamento)
        db.commit()
    return lancamento
