from pydantic import BaseModel, HttpUrl
from datetime import datetime

class UrlCreate(BaseModel):
    url: HttpUrl

class UrlResponse(BaseModel):
    short_code: str
    short_url: str

class UrlAnalytics(BaseModel):
    original_url: str
    short_code: str
    click_count: int
    created_at: datetime
    last_accessed_at: datetime | None = None