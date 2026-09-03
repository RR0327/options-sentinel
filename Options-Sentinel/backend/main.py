from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.routes import router
from backend.dashboard_routes import dashboard_router
from database.database import engine, Base
from database import models

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Options Sentinel API", description="AI Options Trading Agent", version="1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)
app.include_router(dashboard_router)

@app.get("/")
def home():
    return {"project": "Options Sentinel", "status": "running"}
