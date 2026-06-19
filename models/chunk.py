from uuid import uuid4
from pydantic import BaseModel, Field

class Chunk(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid4()))
    text: str
    section_number: str
    section_title: str
    page_number: int