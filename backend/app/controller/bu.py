from sqlalchemy.orm import Session
from fastapi import HTTPException
from starlette import status
from app.model.tables import BusinessUnit
from app.model.tables import Employee
from app.controller.employee import select_employee_by_id

# INPUT
from app.schema.input.bu import BaseBu, BaseBuToUpdate

# OUTPUT
from app.schema.output.bu import BaseModelBu, BaseModelBus


def select_bu(id: int, db: Session) -> BaseModelBu:
    return db.query(BusinessUnit).filter(BusinessUnit.id == id).first()


def select_bu_by_employee_id(employee_id: int, db: Session) -> BaseModelBus:
    data = db.query(Employee).filter(Employee.id == employee_id).scalar()
    return data


def select_list_all_bus(db: Session):
    data = db.query(BusinessUnit).all()
    return data


def insert_bu(buss_u: BaseBu, db: Session) -> BaseModelBu:
    if not select_employee_by_id(id=buss_u.fk_id_employees, db=db):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="O funcionário informado não existe.",
        )
    if (
        db.query(BusinessUnit)
        .filter(
            BusinessUnit.name == buss_u.name,
            BusinessUnit.product_family == buss_u.product_family,
        )
        .first()
    ):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="A BU e familia de produto já existe.",
        )
    bu = BusinessUnit(**buss_u.dict(by_alias=False))
    db.add(bu)
    db.commit()
    db.refresh(bu)
    return bu


def update_bu(id: int, buss_u: BaseBuToUpdate, db: Session) -> BaseModelBu:
    bu = select_bu(id=id, db=db)
    if not bu:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="A BU informada não existe.",
        )
    row = buss_u.dict(exclude_none=True)
    if not row:
        raise HTTPException(
            status_code=status.HTTP_206_PARTIAL_CONTENT,
            detail="Não há dados para ser alterado.",
        )
    db.query(BusinessUnit).filter(BusinessUnit.id == id).update(
        row, synchronize_session=False
    )
    db.commit()
    db.refresh(bu)
    return bu


def delete_bu(id: int, db: Session) -> BaseModelBu:
    if not select_bu(id=id, db=db):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="A BU informada não existe."
        )
    bu = db.query(BusinessUnit).filter(BusinessUnit.id == id).first()
    if bu.month:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Você não pode deletar uma BU que está atrelada a um orçamento.",
        )
    data = BaseModelBu.from_orm(bu)
    db.delete(bu)
    db.commit()
    return data
