from sqlalchemy import Column, Integer, String, Float
from core.banco import Base


class Funcionario(Base):
    __tablename__ = "funcionarios"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100), nullable=False)
    cpf = Column(String(14), nullable=False)
    cargo = Column(String(50), nullable=False)
    salario = Column(Float, nullable=False)

    