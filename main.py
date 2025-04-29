from fastapi import FastAPI
from routes import material, cliente, projeto, fornecedor, funcionario, financeiro

app = FastAPI(title="Sistema de Gestão para Construtoras")

# Incluindo as rotas
app.include_router(material.router, prefix="/materiais")

