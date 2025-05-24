from sqlalchemy import Column, Integer, String, Float
from core.banco import Base

class Fornecedor(Base):
    __tablename__ = "fornecedores"

    id = Column(Integer, primary_key=True, index=True)
    cnpj = Column(String(18), nullable=False)
    nome = Column(String(100), nullable=False)
    contato = Column(String(100), nullable=False)
    tipo_material = Column(String(100), nullable=False)