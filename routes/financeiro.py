from fastapi import APIRouter
from core.banco import get_db
from schemas.financeiro  import FinanceiroCreate, FinanceiroResponse, FinanceiroUpdate
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from models.projeto import Projeto as ProjetoModel
from models.material import Material as MaterialModel
from models.funcionario import Funcionario as FuncionarioModel
from sqlalchemy.orm import Session
from models.financeiro import Financeiro as FinanceiroModel
from services import financeiro_service
from models.projeto import Projeto
from models.material import Material
from models.funcionario import Funcionario

router = APIRouter(prefix="/financeiro", tags=["Financeiro"])

@router.post("/", response_model=FinanceiroResponse)
def criar(dados: FinanceiroCreate, db: Session = Depends(get_db)):
    if dados.projeto_id is not None:
        if not db.query(Projeto).filter(Projeto.id == dados.projeto_id).first():
            raise HTTPException(status_code=404, detail="Projeto não encontrado")

    if dados.material_id is not None:
        if not db.query(Material).filter(Material.id == dados.material_id).first():
            raise HTTPException(status_code=404, detail="Material não encontrado")

    if dados.funcionario_id is not None:
        if not db.query(Funcionario).filter(Funcionario.id == dados.funcionario_id).first():
            raise HTTPException(status_code=404, detail="Funcionário não encontrado")

    return financeiro_service.criar_lancamento(db, dados)

@router.get("/", response_model=list[FinanceiroResponse])
def listar(db: Session = Depends(get_db)):
    return financeiro_service.listar_lancamentos(db)

@router.get("/{lancamento_id}", response_model=FinanceiroResponse)
def buscar(lancamento_id: int, db: Session = Depends(get_db)):
    lancamento = financeiro_service.buscar_lancamento(db, lancamento_id)
    if not lancamento:
        raise HTTPException(status_code=404, detail="Lançamento não encontrado")
    return lancamento

@router.put("/{lancamento_id}", response_model=FinanceiroResponse)
def atualizar(lancamento_id: int, dados: FinanceiroUpdate, db: Session = Depends(get_db)):
    lancamento = financeiro_service.atualizar_lancamento(db, lancamento_id, dados)
    if not lancamento:
        raise HTTPException(status_code=404, detail="Lançamento não encontrado")
    return lancamento

@router.delete("/{lancamento_id}")
def deletar(lancamento_id: int, db: Session = Depends(get_db)):
    lancamento = financeiro_service.deletar_lancamento(db, lancamento_id)
    if not lancamento:
        raise HTTPException(status_code=404, detail="Lançamento não encontrado")
    return {"ok": True, "mensagem": "Lançamento excluído com sucesso"}


@router.get("/resumo/{projeto_id}")
def resumo_financeiro(projeto_id: int, db: Session = Depends(get_db)):
    projeto = db.query(ProjetoModel).filter(ProjetoModel.id == projeto_id).first()
    if not projeto:
        raise HTTPException(status_code=404, detail="Projeto não encontrado")

    # CUSTO MATERIAL
    materiais = db.query(MaterialModel).filter(MaterialModel.projeto_id == projeto_id).all()
    custo_materiais = sum(mat.preco * mat.quantidade for mat in materiais)

    # CUSTO SALARIO
    funcionarios = db.query(FuncionarioModel).filter(FuncionarioModel.projeto_id == projeto_id).all()
    custo_salarios = sum(func.salario for func in funcionarios)

    # CUSTO PREVISTO x CUSTO ATUAL
    custo_previsto = projeto.custo_total
    custo_atual = projeto.custo_atual

    # CUSTO TOTAL
    custo_total_calculado = custo_materiais + custo_salarios

    # DIFERENÇA DE ORÇAMENTO
    diferenca_orcamento = custo_previsto - custo_total_calculado

    return {
        "projeto_id": projeto_id,
        "nome": projeto.nome,
        "status": projeto.status,
        "custo_previsto": custo_previsto,
        "custo_atual_projeto": custo_atual,
        "custo_total_materiais": custo_materiais,
        "custo_total_salarios": custo_salarios,
        "custo_total_geral": custo_total_calculado,
        "diferenca_orcamento": diferenca_orcamento
    }
