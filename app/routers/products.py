from fastapi import APIRouter
from ..database.models import Products
from ..database.db import SessionDep
from sqlmodel import select
from typing import List

router = APIRouter()


@router.get("/products")
def get_all_products(session: SessionDep) -> List[Products]:
    return session.exec(select(Products)).all()
