from datetime import datetime
from pydantic import BaseModel


class CategoryRequest(BaseModel):
    name: str


class CategoryResponse(BaseModel):
    id: str
    name: str
    created_at: datetime
    updated_at: datetime
    is_active: bool
