from pydantic import BaseModel


class CompanyResponse(BaseModel):

    company_id: int

    company_name: str

    industry: str

    company_size: str | None = None

    headquarters: str | None = None

    website: str | None = None

    status: str

    class Config:
        from_attributes = True