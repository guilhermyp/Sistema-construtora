from sqlalchemy import Column, Integer, String, Float
from core.banco import Base

class Projeto(Base):
    __tablename__ = "projetos"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100), nullable=False)
    descricao = Column(String(255), nullable=False)
    data_inicio = Column(String(50), nullable=False)
    data_fim = Column(String(50), nullable=False)
    status = Column(String(50), nullable=False)
    custo_total = Column(Float, nullable=False)
    custo_atual = Column(Float, nullable=False)
    progresso = Column(Float, nullable=False)
    responsavel_projeto = Column(String(100))