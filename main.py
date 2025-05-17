from fastapi import FastAPI
from routes import material, cliente, projeto, fornecedor, funcionario, financeiro
from banco.conexao import engine

from routes import (
    cliente_route,
    financeiro_route,
    fornecedor_route,
    funcionario_route,
    material_route,
    projeto_route
)
from sqlalchemy.orm import declarative_base

app = FastAPI(title="Sistema de Gestão para Construtoras")

# Criação das tabelas
Base = declarative_base()
cliente.Base.metadata.create_all(bind=engine)
financeiro.Base.metadata.create_all(bind=engine)
fornecedor.Base.metadata.create_all(bind=engine)
funcionario.Base.metadata.create_all(bind=engine)
material.Base.metadata.create_all(bind=engine)
projeto.Base.metadata.create_all(bind=engine)

# Rotas
app.include_router(cliente_route.router, prefix="/clientes", tags=["Clientes"])
app.include_router(financeiro_route.router, prefix="/financeiro", tags=["Financeiro"])
app.include_router(fornecedor_route.router, prefix="/fornecedores", tags=["Fornecedores"])
app.include_router(funcionario_route.router, prefix="/funcionarios", tags=["Funcionários"])
app.include_router(material_route.router, prefix="/materiais", tags=["Materiais"])
app.include_router(projeto_route.router, prefix="/projetos", tags=["Projetos"])
