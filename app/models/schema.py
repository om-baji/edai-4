from typing import Optional, Dict, Any

from pydantic import Field, BaseModel, field_validator


class StoryRequest(BaseModel):
    culture: str = Field(..., min_length=2)
    theme: Optional[str] = None
    max_length: Optional[int] = Field(500, ge=100, le=2000)
    language: Optional[str] = "English"
    tone: Optional[str] = "neutral"

    @field_validator('culture')
    def validate_culture(cls, v):
        if len(v.strip()) == 0:
            raise ValueError('Culture cannot be empty')
        return v

class StoryResponse(BaseModel):
    story: str
    character_count: int
    language: str
    metadata: Dict[str, Any]

class Response(BaseModel):
    success: bool
    message: str
    timestamp: str


class SearchQuery:
    pass