from fastapi import APIRouter
from fastapi import Depends
from fastapi import FastAPI
from fastapi import Query
from fastapi import status
from sqlalchemy.orm.session import Session

from app.config.settings import settings
from app.controller import bu
from app.model.database import get_db


# INPUT
from app.schema.input.bu import BaseBu, BaseBuToUpdate

# OUTPUT
from app.schema.output.bu import BaseModelBu
from app.schema.output.bu import BaseModelBus


def init_app(app: FastAPI):
    router = APIRouter()

    @router.post(
        "/bu",
        response_model=BaseModelBu,
        status_code=status.HTTP_201_CREATED,
    )
    async def post_bu(buss_u: BaseBu, db: Session = Depends(get_db)):
        return bu.insert_bu(buss_u=buss_u, db=db)

    @router.get("/bu", response_model=Union[BaseModelBus, List[BaseModelBu]])
    async def get_bu_by_employee_id(
        employee_id: int = Query(...), db: Session = Depends(get_db)
    ):
        return bu.select_bu_by_employee_id(employee_id=employee_id, db=db)

    @router.get("/bu/all", response_model=List[BaseModelBu])
    async def get_bu_by_employee_id(db: Session = Depends(get_db)):
        return bu.select_list_all_bus(db=db)

    @router.get("/bu/{id}", response_model=BaseModelBu)
    async def get_bu(id: int, db: Session = Depends(get_db)):
        return bu.select_bu(id=id, db=db)

    @router.patch("/bu/{id}", response_model=BaseModelBu)
    async def patch_bu(id: int, buss_u: BaseBuToUpdate, db: Session = Depends(get_db)):
        return bu.update_bu(id=id, buss_u=buss_u, db=db)

    @router.delete("/bu/{id}", response_model=BaseModelBu)
    async def delete_bu(id: int, db: Session = Depends(get_db)):
        return bu.delete_bu(id=id, db=db)

    app.include_router(router=router, prefix=settings.api_v1, tags=["Business Unit"])
