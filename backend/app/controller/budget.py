from app.schema.output.budget import BaseModelBudgetEmployee, BaseModelBudgetsEmployee
from fastapi import HTTPException, status
from app.schema.input.budget import BaseBudget
from sqlalchemy.orm.session import Session
from app.model.tables import Employee, Budget
from app.controller.employee import select_employee_by_id


def select_budget_by_name(budget_name: str, db: Session) -> bool:
    return True if db.query(Budget).filter(Budget.name == budget_name).first() else False


def insert_budget(bud: BaseBudget, db: Session):
    if select_budget_by_name(budget_name=bud.name, db=db):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Já existe um orçamento com este nome.",
        )
    if not select_employee_by_id(id=bud.fk_id_employees, db=db):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="O funcionário informado não existe.",
        )
    budget = Budget(**bud.dict(by_alias=False))
    db.add(budget)
    db.commit()
    db.refresh(budget)
    return budget


def select_budgets_by_employee_id(
    employee_id: int, db: Session
) -> BaseModelBudgetsEmployee:
    data = db.query(Employee).filter(Employee.id == employee_id).scalar()
    budget = [bud for bud in data.budget if bud.month]
    data.budget = budget
    return data


def select_budget_by_budget_id(budget_id: int, db: Session) -> BaseModelBudgetEmployee:
    data = db.query(Budget).filter(Budget.id == budget_id).first()
    return data


def delete_budget_by_id(budget_id: int, db: Session) -> BaseModelBudgetEmployee:
    budget = select_budget_by_budget_id(budget_id=budget_id, db=db)
    if not budget:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="O orçamento informado não existe.",
        )
    base_model = BaseModelBudgetEmployee.from_orm(budget)
    db.delete(budget)
    db.commit()
    return base_model


def update_budget_by_id(
    budget_id: int, bud: BaseBudget, db: Session
) -> BaseModelBudgetEmployee:
    budget = select_budget_by_budget_id(budget_id=budget_id, db=db)
    if not budget:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="O orçamento informado não existe.",
        )
    if budget.name == bud.name:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="O orçamento informado já existe. Não há nada a ser alterado.",
        )
    if not select_employee_by_id(id=bud.fk_id_employees, db=db):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="O funcionário informado não existe.",
        )
    db.query(Budget).filter(Budget.id == budget_id).update(
        bud.dict(by_alias=False), synchronize_session=False
    )
    db.commit()
    db.refresh(budget)
    return budget
