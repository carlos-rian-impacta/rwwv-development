from pydantic.fields import Field
from app.model.enum import EnumMonthType, EnumMonths
from pydantic import BaseModel
from datetime import datetime


class BaseMonthDefault(BaseModel):
    month: EnumMonths
    year: int = Field(
        ge=datetime.now().year,
        le=datetime.now().year + 1,
        default_factory=lambda: datetime.now().year,
    )
    value: float
    cost: float = None
    type: EnumMonthType
    description: str = None
    comment: str = None


class BaseMonth(BaseMonthDefault):
    fk_id_business_unit: int = Field(..., alias="bu_id", ge=1)
    fk_id_budget: int = Field(..., alias="budget_id", ge=1)


class BaseMonthUpdate(BaseModel):
    month: EnumMonths = None
    year: int = Field(None, ge=datetime.now().year, le=datetime.now().year + 1)
    value: float = None
    cost: float = None
    type: EnumMonthType = None
    description: str = None
    comment: str = None
    fk_id_business_unit: int = Field(None, alias="bu_id", ge=1)
    fk_id_budget: int = Field(None, alias="budget_id", ge=1)
