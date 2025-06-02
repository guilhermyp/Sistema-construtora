from sqlalchemy.orm import Session
from models.material import Material
from schemas.material import MaterialCreate, MaterialUpdate


def criar_material(db: Session, material_data: MaterialCreate):
    novo_material = Material(**material_data.dict())
    db.add(novo_material)
    db.commit()
    db.refresh(novo_material)
    return novo_material


def listar_materiais(db: Session):
    return db.query(Material).all()


def buscar_material(db: Session, material_id: int):
    return db.query(Material).filter(Material.id == material_id).first()


def atualizar_material(db: Session, material_id: int, material_data: MaterialUpdate):
    material = db.query(Material).filter(Material.id == material_id).first()
    if material:
        for campo, valor in material_data.dict(exclude_unset=True).items():
            setattr(material, campo, valor)
        db.commit()
        db.refresh(material)
    return material


def deletar_material(db: Session, material_id: int):
    material = db.query(Material).filter(Material.id == material_id).first()
    if material:
        db.delete(material)
        db.commit()
    return material
