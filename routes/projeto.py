
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas.projeto import ProjetoCreate, ProjetoResponse
from fastapi import Depends, HTTPException
from core.banco import get_db
from schemas.projeto import ProjetoCreate, ProjetoResponse
from models.Projeto import Projeto as ProjetoModel


router = APIRouter(prefix="/projetos", tags=["Projeto"])

@router.post("/")
def criar_projeto(projeto: ProjetoCreate, db: Session = Depends(get_db)):
    db_projeto = ProjetoModel(**projeto.model_dump())
    db.add(db_projeto)
    db.commit()
    db.refresh(db_projeto)
    return db_projeto