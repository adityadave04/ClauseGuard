from pydantic import BaseModel


class ContractMetadata(BaseModel):
    agreement_number: str
    service_provider: str
    client: str
    governing_law: str
    payment_terms_days: int
    notice_period_days: int
    termination_fee_percent: float
    uptime_sla_percent: float