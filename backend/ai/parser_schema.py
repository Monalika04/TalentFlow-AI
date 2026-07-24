from enum import Enum
from typing import List

from pydantic import BaseModel, ConfigDict, EmailStr, Field, HttpUrl


# ==========================================================
# ENUMS
# ==========================================================

class SeniorityLevel(str, Enum):
    INTERN = "INTERN"
    FRESHER = "FRESHER"
    JUNIOR = "JUNIOR"
    MID = "MID"
    SENIOR = "SENIOR"
    LEAD = "LEAD"


class InterviewReadiness(str, Enum):
    READY = "READY"
    ALMOST_READY = "ALMOST_READY"
    NEEDS_IMPROVEMENT = "NEEDS_IMPROVEMENT"


# ==========================================================
# FACTS
# ==========================================================

class PersonalInformation(BaseModel):
    model_config = ConfigDict(extra="forbid")

    full_name: str | None = None
    email: EmailStr | None = None
    phone: str | None = None
    location: str | None = None
    linkedin: HttpUrl | None = None
    github: HttpUrl | None = None
    portfolio: HttpUrl | None = None


class Education(BaseModel):
    model_config = ConfigDict(extra="forbid")

    degree: str
    institution: str
    specialization: str | None = None
    cgpa: float | None = None
    percentage: float | None = None
    passing_year: int | None = None


class Experience(BaseModel):
    model_config = ConfigDict(extra="forbid")

    company: str
    designation: str

    start_date: str | None = None
    end_date: str | None = None

    responsibilities: List[str] = Field(default_factory=list)

    technologies: List[str] = Field(default_factory=list)


class Project(BaseModel):
    model_config = ConfigDict(extra="forbid")

    title: str
    description: str

    technologies: List[str] = Field(default_factory=list)

    github_url: HttpUrl | None = None
    live_url: HttpUrl | None = None


class TechnicalSkills(BaseModel):
    model_config = ConfigDict(extra="forbid")

    programming_languages: List[str] = Field(default_factory=list)

    frameworks: List[str] = Field(default_factory=list)

    databases: List[str] = Field(default_factory=list)

    cloud: List[str] = Field(default_factory=list)

    tools: List[str] = Field(default_factory=list)

    libraries: List[str] = Field(default_factory=list)


class Certification(BaseModel):
    model_config = ConfigDict(extra="forbid")

    name: str
    issuer: str | None = None
    issue_date: str | None = None


class Language(BaseModel):
    model_config = ConfigDict(extra="forbid")

    name: str
    proficiency: str | None = None


class ResumeFacts(BaseModel):
    model_config = ConfigDict(extra="forbid")

    personal_information: PersonalInformation

    education: List[Education] = Field(default_factory=list)

    experience: List[Experience] = Field(default_factory=list)

    projects: List[Project] = Field(default_factory=list)

    technical_skills: TechnicalSkills

    soft_skills: List[str] = Field(default_factory=list)

    certifications: List[Certification] = Field(default_factory=list)

    languages: List[Language] = Field(default_factory=list)

    achievements: List[str] = Field(default_factory=list)


# ==========================================================
# AI INTELLIGENCE
# ==========================================================

class ResumeIntelligence(BaseModel):
    model_config = ConfigDict(extra="forbid")

    professional_summary: str

    candidate_strengths: List[str] = Field(default_factory=list)

    improvement_areas: List[str] = Field(default_factory=list)

    recommended_roles: List[str] = Field(default_factory=list)

    seniority_level: SeniorityLevel

    estimated_years_of_experience: float

    ats_score: float = Field(ge=0, le=100)

    interview_readiness: InterviewReadiness

    learning_recommendations: List[str] = Field(default_factory=list)

    confidence_score: float = Field(ge=0, le=1)


# ==========================================================
# ROOT RESPONSE
# ==========================================================

class ResumeAIResponse(BaseModel):
    model_config = ConfigDict(extra="forbid")

    facts: ResumeFacts

    intelligence: ResumeIntelligence