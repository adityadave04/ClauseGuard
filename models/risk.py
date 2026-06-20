from pydantic import BaseModel


class RiskItem(BaseModel):
    severity: str
    section_number: str
    title: str
    issue: str
    recommendation: str