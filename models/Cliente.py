from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from core.banco import Base
from pydantic import BaseModel

class Cliente(Base):
    __tablename__ = "clientes"

    id = Column(Integer, primary_key=True, index=True)
    cpf = Column(String(100), nullable=False)
    cnpj = Column(String(100), nullable=False)
    nome = Column(String(100), nullable=False)
    contato = Column(String(100), nullable=False)
    projeto_id = Column(String(100), nullable=False)
    
    projeto_id = Column(Integer, ForeignKey("projetos.id"), nullable=True)  # Relacionamento
    projeto = relationship("Projeto", backref="clientes")