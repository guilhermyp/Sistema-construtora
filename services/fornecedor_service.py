from sqlalchemy.orm import Session
from models.fornecedor import Fornecedor
from models.fornecedor import Fornecedor as FornecedorModel
from schemas.fornecedor import FornecedorCreate, FornecedorResponse, FornecedorUpdate
def criar_fornecedor(db: Session, fornecedor: FornecedorCreate):
    db_forn = Fornecedor(**fornecedor.model_dump())
    db.add(db_forn)
    db.commit()
    db.refresh(db_forn)
    return db_forn

def listar_fornecedores(db: Session):
    return db.query(Fornecedor).all()

def buscar_fornecedor(db: Session, fornecedor_id: int):
    return db.query(Fornecedor).filter(Fornecedor.id == fornecedor_id).first()

def atualizar_fornecedor(db: Session, fornecedor_id: int, dados: FornecedorUpdate):
    fornecedor = db.query(FornecedorModel).filter(FornecedorModel.id == fornecedor_id).first()
    if fornecedor:
        for key, value in dados.dict(exclude_unset=True).items():
            setattr(fornecedor, key, value)
        db.commit()
        db.refresh(fornecedor)
    return fornecedor

def deletar_fornecedor(db: Session, fornecedor_id: int):
    fornecedor = buscar_fornecedor(db, fornecedor_id)
    if not fornecedor:
        return None
    db.delete(fornecedor)
    db.commit()
    return fornecedor