from fastapi import FastAPI

from app.api import vulnerabilities

from app.api import containers

from fastapi.middleware.cors import CORSMiddleware

from app.api import auth

from app.database.db import engine

from app.models.user import Base

from app.api import monitoring

from app.api import ai

from app.api import threats

from prometheus_client import make_asgi_app

from app.api import metrics

from app.api import falco

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.add_middleware(

    CORSMiddleware,

    allow_origins=[
        "http://localhost:3000"
    ],

    allow_credentials=True,

    allow_methods=["*"],

    allow_headers=["*"],
)

app.include_router(auth.router)
app.include_router(containers.router)
app.include_router(vulnerabilities.router)
app.include_router(monitoring.router)
app.include_router(ai.router)
app.include_router(threats.router)
app.include_router(falco.router)

from app.api import metrics
metrics_app = make_asgi_app()

app.mount(
    "/metrics",
    metrics_app
)
