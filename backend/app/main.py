from fastapi import FastAPI
from app.config import cors
from app.resource import employee
from app.model import tables


def create_app():
    app = FastAPI(
        title="backend rwwv",
        version="0.1.0",
        description="Backend para gerenciamento de orçamento.",
    )
    cors.init_app(app=app)
    tables.init_app(app=app)
    employee.init_app(app=app)
    return app


app = create_app()
