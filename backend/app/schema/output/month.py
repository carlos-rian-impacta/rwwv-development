from pydantic.fields import Field
from app.schema.output.bu import BaseModelBu
from datetime import datetime
from pydantic import validator
from app.schema.input.month import BaseMonthDefault
from app.schema.input.common.budget import BaseModelBudgetEmployee


class BaseModelMonthDefault(BaseMonthDefault):
    id: int
    fk_id_budget: int = Field(None, alias="budget_id")
    fk_id_business_unit: int = Field(None, alias="bu_id")
    created_at: datetime
    updated_at: datetime

    @validator("created_at", "updated_at")
    def validade_datetime(cls, v):
        return f"{v}"

    class Config:
        orm_mode = True
        allow_population_by_field_name = True


class BaseModelMonth(BaseModelMonthDefault):
    budget: BaseModelBudgetEmployee
    business: BaseModelBu
