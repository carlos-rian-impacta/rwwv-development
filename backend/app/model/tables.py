import sqlalchemy
from fastapi import FastAPI
from datetime import datetime

from app.config.settings import settings
from app.model.database import Base
from app.model.enum import (
    EnumBudgetStatus,
    EnumEmploymentType,
    EnumMonths,
    EnumMonthType,
)

# TABLES


# Documentation:
#   - Relationship: https://docs.sqlalchemy.org/en/14/orm/basic_relationships.html
#   - FastAPI SQLAlchemy: https://fastapi.tiangolo.com/tutorial/sql-databases/?h=sqlal#create-the-sqlalchemy-engine


# relationship with token, bu and budget
# Employee 1 - N Token
# Employee 1 - N BusinessUnit
# Employee 1 - 1 Budget
class Employee(Base):
    __tablename__ = "employees"
    # access
    id = sqlalchemy.Column(sqlalchemy.BigInteger, primary_key=True, autoincrement=True)
    email = sqlalchemy.Column(sqlalchemy.String(256), nullable=True, unique=True)
    password = sqlalchemy.Column(sqlalchemy.String(32), nullable=True)
    # personal
    # cpf = sqlalchemy.Column(sqlalchemy.String(11), nullable=False)
    first_name = sqlalchemy.Column(sqlalchemy.String(50), nullable=False)
    last_name = sqlalchemy.Column(sqlalchemy.String(100), nullable=False)
    birth_date = sqlalchemy.Column(sqlalchemy.Date, nullable=True)
    position = sqlalchemy.Column(sqlalchemy.Enum(EnumEmploymentType), nullable=False)
    # permission
    first_access = sqlalchemy.Column(sqlalchemy.Boolean, default=True, nullable=True)
    active = sqlalchemy.Column(sqlalchemy.Boolean, default=False)
    can_simulate_budget = sqlalchemy.Column(sqlalchemy.Boolean, default=False)
    can_submit_budget = sqlalchemy.Column(sqlalchemy.Boolean, default=False)
    can_approve_budget = sqlalchemy.Column(sqlalchemy.Boolean, default=False)
    can_read_budget = sqlalchemy.Column(sqlalchemy.Boolean, default=False)
    is_admin = sqlalchemy.Column(sqlalchemy.Boolean, default=False)
    # datetime
    created_at = sqlalchemy.Column(
        sqlalchemy.DateTime, default=datetime.now, nullable=False
    )
    updated_at = sqlalchemy.Column(
        sqlalchemy.DateTime,
        default=datetime.now,
        onupdate=datetime.now,
        nullable=False,
    )
    # relationship back_populates
    tokens = sqlalchemy.orm.relationship("Token", back_populates="user")
    business = sqlalchemy.orm.relationship("BusinessUnit", back_populates="employee")
    budget = sqlalchemy.orm.relationship("Budget", back_populates="employee")
    approver = sqlalchemy.orm.relationship(
        "Approver", back_populates="approver", uselist=False
    )


# Token N - 1 Employee
class Token(Base):
    __tablename__ = "token"
    # default
    id = sqlalchemy.Column(sqlalchemy.BigInteger, primary_key=True, autoincrement=True)
    access_token = sqlalchemy.Column(sqlalchemy.Text, nullable=False)
    refresh_token = sqlalchemy.Column(sqlalchemy.Text, nullable=False)
    enable = sqlalchemy.Column(sqlalchemy.Boolean, nullable=False, default=True)
    exp = sqlalchemy.Column(sqlalchemy.DateTime, nullable=False)
    # datetime
    created_at = sqlalchemy.Column(
        sqlalchemy.DateTime, default=datetime.now, nullable=False
    )
    updated_at = sqlalchemy.Column(
        sqlalchemy.DateTime,
        default=datetime.now,
        onupdate=datetime.now,
        nullable=False,
    )
    # fks
    fk_id_employees = sqlalchemy.Column(
        sqlalchemy.BigInteger,
        sqlalchemy.ForeignKey("employees.id", ondelete="CASCADE"),
        nullable=False,
    )
    # relationship
    user = sqlalchemy.orm.relationship(
        "Employee", back_populates="tokens", uselist=False
    )


# BusinessUnit N - 1 Employee
# BusinessUnit 1 - N Month
class BusinessUnit(Base):
    __tablename__ = "business_unit"
    # defaults
    id = sqlalchemy.Column(sqlalchemy.BigInteger, primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String(100), nullable=False)
    product_family = sqlalchemy.Column(sqlalchemy.String(100), nullable=False)
    description = sqlalchemy.Column(sqlalchemy.Text, nullable=True)
    # datetime
    created_at = sqlalchemy.Column(
        sqlalchemy.DateTime, default=datetime.now, nullable=False
    )
    updated_at = sqlalchemy.Column(
        sqlalchemy.DateTime,
        default=datetime.now,
        onupdate=datetime.now,
        nullable=False,
    )
    # fks
    fk_id_employees = sqlalchemy.Column(
        sqlalchemy.BigInteger,
        sqlalchemy.ForeignKey("employees.id", ondelete="CASCADE"),
        nullable=False,
    )
    # relationship
    employee = sqlalchemy.orm.relationship(
        "Employee", back_populates="business", uselist=False
    )
    month = sqlalchemy.orm.relationship("Month", back_populates="business")


# Budget N - 1 Employee
# Budget 1 - N StatusBudget
# Budget 1 - N Month
class Budget(Base):
    __tablename__ = "budget"
    # defaults
    id = sqlalchemy.Column(sqlalchemy.BigInteger, primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String(100), nullable=False)
    # datetime
    created_at = sqlalchemy.Column(
        sqlalchemy.DateTime, default=datetime.now, nullable=False
    )
    updated_at = sqlalchemy.Column(
        sqlalchemy.DateTime,
        default=datetime.now,
        onupdate=datetime.now,
        nullable=False,
    )
    # fks
    fk_id_employees = sqlalchemy.Column(
        sqlalchemy.BigInteger,
        sqlalchemy.ForeignKey("employees.id", ondelete="CASCADE"),
        nullable=False,
    )
    # relationship
    employee = sqlalchemy.orm.relationship(
        "Employee", back_populates="budget", uselist=False
    )
    status = sqlalchemy.orm.relationship("StatusBudget", back_populates="budget")
    month = sqlalchemy.orm.relationship("Month", back_populates="budget")
    approver = sqlalchemy.orm.relationship(
        "Approver", back_populates="budget", uselist=False
    )


# Month N - 1 Budget
# Month N - 1 BusinessUnit
class Month(Base):
    __tablename__ = "months"
    # default
    id = sqlalchemy.Column(sqlalchemy.BigInteger, primary_key=True, autoincrement=True)
    month = sqlalchemy.Column(sqlalchemy.Enum(EnumMonths), nullable=False, index=True)
    year = sqlalchemy.Column(
        sqlalchemy.Integer,
        default=lambda: datetime.now().year,
        nullable=False,
        index=True,
    )
    value = sqlalchemy.Column(sqlalchemy.Numeric(18, 2), nullable=False)
    cost = sqlalchemy.Column(sqlalchemy.Numeric(18, 2), nullable=True, default=0)
    type = sqlalchemy.Column(sqlalchemy.Enum(EnumMonthType), nullable=False)
    description = sqlalchemy.Column(sqlalchemy.Text, nullable=True)
    comment = sqlalchemy.Column(sqlalchemy.Text, nullable=True)
    # datetime
    created_at = sqlalchemy.Column(
        sqlalchemy.DateTime, default=datetime.now, nullable=False
    )
    updated_at = sqlalchemy.Column(
        sqlalchemy.DateTime,
        default=datetime.now,
        onupdate=datetime.now,
        nullable=False,
    )
    # fks
    fk_id_business_unit = sqlalchemy.Column(
        sqlalchemy.BigInteger,
        sqlalchemy.ForeignKey("business_unit.id", ondelete="CASCADE"),
        nullable=False,
    )

    fk_id_budget = sqlalchemy.Column(
        sqlalchemy.BigInteger,
        sqlalchemy.ForeignKey("budget.id", ondelete="CASCADE"),
        nullable=False,
    )
    # relationship
    budget = sqlalchemy.orm.relationship("Budget", back_populates="month", uselist=False)
    business = sqlalchemy.orm.relationship(
        "BusinessUnit", back_populates="month", uselist=False
    )


# Budget 1 - N StatusBudget
class StatusBudget(Base):
    __tablename__ = "status_budget"
    # default
    id = sqlalchemy.Column(sqlalchemy.BigInteger, primary_key=True, autoincrement=True)
    status = sqlalchemy.Column(
        sqlalchemy.Enum(EnumBudgetStatus), default=EnumBudgetStatus.draft, nullable=False
    )
    current = sqlalchemy.Column(sqlalchemy.Boolean, nullable=False, default=True)
    message = sqlalchemy.Column(sqlalchemy.Text, nullable=True)
    # datetime
    created_at = sqlalchemy.Column(
        sqlalchemy.DateTime, default=datetime.now, nullable=False
    )
    updated_at = sqlalchemy.Column(
        sqlalchemy.DateTime,
        default=datetime.now,
        onupdate=datetime.now,
        nullable=False,
    )
    # fks
    fk_id_budget = sqlalchemy.Column(
        sqlalchemy.BigInteger,
        sqlalchemy.ForeignKey("budget.id", ondelete="CASCADE"),
        nullable=False,
    )
    # relationship
    budget = sqlalchemy.orm.relationship(
        "Budget", back_populates="status", uselist=False
    )


class Approver(Base):
    __tablename__ = "approver"
    id = sqlalchemy.Column(sqlalchemy.BigInteger, primary_key=True, autoincrement=True)
    created_at = sqlalchemy.Column(
        sqlalchemy.DateTime, default=datetime.now, nullable=False
    )
    updated_at = sqlalchemy.Column(
        sqlalchemy.DateTime,
        default=datetime.now,
        onupdate=datetime.now,
        nullable=False,
    )
    # fks
    fk_id_budget = sqlalchemy.Column(
        sqlalchemy.BigInteger,
        sqlalchemy.ForeignKey("budget.id", ondelete="CASCADE"),
        nullable=False,
    )
    fk_id_approver = sqlalchemy.Column(
        sqlalchemy.BigInteger,
        sqlalchemy.ForeignKey("employees.id", ondelete="CASCADE"),
        nullable=False,
    )
    # relationship
    budget = sqlalchemy.orm.relationship("Budget", back_populates="approver")
    approver = sqlalchemy.orm.relationship(
        "Employee", back_populates="approver", uselist=False
    )


def drop_table():
    engine = sqlalchemy.create_engine(settings.database_uri, echo=True)
    Base.metadata.drop_all(bind=engine, checkfirst=True)


def create_table():
    engine = sqlalchemy.create_engine(settings.database_uri, echo=True)
    Base.metadata.create_all(bind=engine)


def insert():
    engine = sqlalchemy.create_engine(settings.database_uri, echo=True)
    with open("extra/insert.sql", mode="r") as file:
        sql = file.read()
        engine.execute(sql)


def init_app(app: FastAPI):
    # drop_table()
    # create_table()
    # insert()
    ...
