from sqlalchemy.orm import Session
from models.projeto import Projeto
from schemas.projeto import ProjetoCreate, ProjetoUpdate, ProjetoResponse
from models.funcionario import Funcionario


def criar_projeto(db: Session, projeto_data):
    funcionarios_ids = projeto_data.funcionarios_ids
    dados_projeto = projeto_data.dict(exclude={"funcionarios_ids"})
    
    novo_projeto = Projeto(**dados_projeto)

    if funcionarios_ids:
        funcionarios = db.query(Funcionario).filter(Funcionario.id.in_(funcionarios_ids)).all()
        novo_projeto.funcionarios = funcionarios

    db.add(novo_projeto)
    db.commit()
    db.refresh(novo_projeto)
    return novo_projeto


def listar_projetos(db: Session):
    return db.query(Projeto).all()


def buscar_projeto(db: Session, projeto_id: int):
    return db.query(Projeto).filter(Projeto.id == projeto_id).first()


def atualizar_projeto(db: Session, projeto_id: int, projeto_data: ProjetoUpdate):
    projeto = db.query(Projeto).filter(Projeto.id == projeto_id).first()
    if projeto:
        for campo, valor in projeto_data.dict(exclude_unset=True).items():
            setattr(projeto, campo, valor)
        db.commit()
        db.refresh(projeto)
    return projeto


def deletar_projeto(db: Session, projeto_id: int):
    projeto = db.query(Projeto).filter(Projeto.id == projeto_id).first()
    if projeto:
        db.delete(projeto)
        db.commit()
    return projeto
