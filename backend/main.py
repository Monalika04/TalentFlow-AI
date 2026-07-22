from fastapi import FastAPI

from backend.api.company import router as company_router
from backend.api.candidate import router as candidate_router

app = FastAPI(
    title="TalentFlow AI",
    version="1.0.0"
)

app.include_router(company_router)
app.include_router(candidate_router)


@app.get("/")
def home():

    return {
        "message": "Welcome to TalentFlow AI 🚀"
    }