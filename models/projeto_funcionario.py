from sqlalchemy import Table, Column, Integer, ForeignKey
from core.banco import Base

projeto_funcionario = Table(
    "projeto_funcionario",
    Base.metadata,
    Column("projeto_id", ForeignKey("projetos.id"), primary_key=True),
    Column("funcionario_id", ForeignKey("funcionarios.id"), primary_key=True)
)