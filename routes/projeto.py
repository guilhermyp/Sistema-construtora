
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas.projeto import ProjetoCreate, ProjetoResponse
from fastapi import Depends, HTTPException
from core.banco import get_db
from schemas.projeto import ProjetoCreate, ProjetoResponse, ProjetoUpdate, ProjetoComMateriaisResponse
from models.projeto import Projeto as ProjetoModel
from services import projeto_service
from models.material import Material as MaterialModel
from models.funcionario import Funcionario as FuncionarioModel
from services.projeto_service import criar_projeto, atualizar_projeto

router = APIRouter(prefix="/projetos", tags=["Projeto"])

@router.post("/", response_model=ProjetoResponse)
def criar(projeto_in: ProjetoCreate, db: Session = Depends(get_db)):
    # Opcional: validar funcionários recebidos
    if projeto_in.funcionarios_ids:
        funcionarios = db.query(FuncionarioModel).filter(FuncionarioModel.id.in_(projeto_in.funcionarios_ids)).all()
        if len(funcionarios) != len(projeto_in.funcionarios_ids):
            raise HTTPException(status_code=404, detail="Funcionário não foi encontrado")
    projeto = criar_projeto(db, projeto_in)
    return projeto

# LISTAR PROJETOS
@router.get("/", response_model=list[ProjetoResponse])
def listar(db: Session = Depends(get_db)):
    return projeto_service.listar_projetos(db)

# BUSCAR PROJETO POR ID
@router.get("/{projeto_id}", response_model=ProjetoComMateriaisResponse)
def buscar_com_materiais(projeto_id: int, db: Session = Depends(get_db)):
    projeto = db.query(ProjetoModel).filter(ProjetoModel.id == projeto_id).first()
    if not projeto:
        raise HTTPException(status_code=404, detail="Projeto não encontrado")

    materiais = db.query(MaterialModel).filter(MaterialModel.projeto_id == projeto_id).all()

    return {
        **projeto.__dict__,
        "materiais": materiais
    }

# ATUALIZAR PROJETO POR ID
@router.put("/{projeto_id}", response_model=ProjetoResponse)
def atualizar(projeto_id: int, projeto_in: ProjetoUpdate, db: Session = Depends(get_db)):
    if projeto_in.funcionarios_ids:
        funcionarios = db.query(FuncionarioModel).filter(FuncionarioModel.id.in_(projeto_in.funcionarios_ids)).all()
        if len(funcionarios) != len(projeto_in.funcionarios_ids):
            raise HTTPException(status_code=404, detail="Funcionário não foi encontrado")
    projeto = atualizar_projeto(db, projeto_id, projeto_in)
    if projeto is None:
        raise HTTPException(status_code=404, detail="Projeto não encontrado")
    return projeto

# DELETAR PROJETO POR ID
@router.delete("/{projeto_id}")
def deletar(projeto_id: int, db: Session = Depends(get_db)):
    projeto = projeto_service.deletar_projeto(db, projeto_id)
    if not projeto:
        raise HTTPException(status_code=404, detail="Projeto não encontrado")
    return {"ok": True, "mensagem": "Projeto excluído com sucesso"}

