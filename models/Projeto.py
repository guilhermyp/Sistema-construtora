from sqlalchemy import Column, Integer, String, Float
from core.banco import Base
from sqlalchemy.orm import relationship
from models.projeto_funcionario import projeto_funcionario

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


    materiais = relationship("Material", back_populates="projeto")
    funcionarios = relationship("Funcionario", secondary=projeto_funcionario, backref="projetos")