from fastapi import FastAPI

from backend.api.company import router as company_router
from backend.api.candidate import router as candidate_router
from backend.api.skill import router as skill_router
from backend.api.candidate_skill import router as candidate_skill_router
from backend.api.job import router as job_router
from backend.api.job_skill import router as job_skill_router
from backend.api.resume import router as resume_router
from backend.api.application import router as application_router
from backend.api.application_status_history_api import (
    router as application_status_history_router,
)
from backend.api.ai_recommendation_api import (
    router as ai_recommendation_router,
)
from backend.exceptions.handlers import (
    register_exception_handlers,
)

from backend.authentication.auth_api import router as auth_router
from backend.api.recruiter_api import router as recruiter_router
app = FastAPI(
    title="TalentFlow AI",
    version="1.0.0"
)
register_exception_handlers(app)

app.include_router(company_router)
app.include_router(candidate_router)
app.include_router(skill_router)
app.include_router(candidate_skill_router)
app.include_router(job_router)
app.include_router(job_skill_router)
app.include_router(resume_router)
app.include_router(application_router)
app.include_router(application_status_history_router)
app.include_router(ai_recommendation_router)
app.include_router(recruiter_router)
app.include_router(auth_router)

@app.get("/")
def home():

    return {
        "message": "Welcome to TalentFlow AI 🚀"
    }