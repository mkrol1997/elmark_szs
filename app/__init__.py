from fastapi import FastAPI

from app.pim.routes import router as pim_router

app = FastAPI()

app.include_router(pim_router)
