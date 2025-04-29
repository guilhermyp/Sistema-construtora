from fastapi import APIRouter, HTTPException
from models.material import Material
from typing import List


router = APIRouter()

@router.post("/", response_model=Material)
def cadastrar_material(material: Material):
   
   
