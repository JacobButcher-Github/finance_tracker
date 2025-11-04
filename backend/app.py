# uv/pdm
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# local
from expenditure.expenditure_router import expenditure_router
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
