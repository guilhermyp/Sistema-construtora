from fastapi import FastAPI
from routes import material, cliente, projeto, fornecedor, funcionario, financeiro
from core.banco import engine, Base

app = FastAPI(title="Sistema de Gestão para Construtoras")

# Criação das tabelas
Base.metadata.create_all(bind=engine)

# Rotas
app.include_router(cliente.router, prefix="/clientes", tags=["Clientes"])
app.include_router(financeiro.router, prefix="/financeiro", tags=["Financeiro"])
app.include_router(fornecedor.router, prefix="/fornecedores", tags=["Fornecedores"])
app.include_router(funcionario.router, prefix="/funcionario", tags=["Funcionário"])
app.include_router(material.router, prefix="/materiais", tags=["Materiais"])
app.include_router(projeto.router, prefix="/projetos", tags=["Projetos"])
