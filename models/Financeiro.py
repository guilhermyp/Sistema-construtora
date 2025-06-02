from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey
from sqlalchemy.orm import relationship
from core.banco import Base

class Financeiro(Base):
    __tablename__ = "financeiro"

    id = Column(Integer, primary_key=True, index=True)
    tipo = Column(String(100), nullable=False)  # SALARIO, PROJETO, MATERIAL eTC
    descricao = Column(String(100))
    valor = Column(Float, nullable=False)
    data = Column(Date, nullable=False)

    funcionario_id = Column(Integer, ForeignKey("funcionarios.id", ondelete="SET NULL"), nullable=True)
    projeto_id = Column(Integer, ForeignKey("projetos.id", ondelete="SET NULL"), nullable=True)
    material_id = Column(Integer, ForeignKey("materiais.id", ondelete="SET NULL"), nullable=True)

    funcionario = relationship("Funcionario", backref="lancamentos_financeiros")
    projeto = relationship("Projeto", backref="lancamentos_financeiros")
    material = relationship("Material", backref="lancamentos_financeiros")
