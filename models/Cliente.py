from sqlalchemy import Column, Integer, String, Float
from core.banco import Base
from pydantic import BaseModel

class Cliente(Base):
    __tablename__ = "clientes"

    id = Column(Integer, primary_key=True, index=True)
    cpf = Column(String(100), nullable=False)
    cnpj = Column(String(100), nullable=False)
    nome = Column(String(100), nullable=False)
    projeto = Column(String(100), nullable=False)
    contato = Column(String(100), nullable=False)
    