# uv/pdm
from fastapi import FastAPI, Request, status
from fastapi.middleware.cors import CORSMiddleware

from expenditure.expenditure_router import expenditure_router
# local
from income.income_router import income_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(income_router)
app.include_router(expenditure_router)
