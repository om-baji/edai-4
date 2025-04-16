from enum import Enum
from typing import Optional, Dict, Any, List

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

class RolePlayRequest(BaseModel):
    culture: str
    role: str
    era: str
    tone: str
    language: str
    include_emotion: bool
    chat_history: List[Dict[str, str]]  # [{"user": "Hi!", "ai": "Hello, traveler!"}, ...]
    user_input: str  # current user message

class SentimentRequest(BaseModel):
    story : str

class SentimentResponse(BaseModel):
    tone : str
    culture : str
    sentiment_score : int
class SearchQuery:
    pass

class DebateRequest(BaseModel):
    user_response: str
    prompt: str


class DebatePromptResponse(BaseModel):
    prompt: str
    timestamp: str


class DebateEvaluationResponse(BaseModel):
    evaluation: str
    scores: Dict[str, float]
    suggestions: Optional[str] = None
    timestamp: str

class ConflictType(str, Enum):
    INDIA_PAKISTAN = "india_pakistan"
    ISRAELI_PALESTINIAN = "israeli_palestinian"
    INDIGENOUS_RIGHTS = "indigenous_rights"
    NORTHERN_IRELAND = "northern_ireland"
    RWANDA = "rwanda"


class Role(str, Enum):
    MEDIATOR = "mediator"
    DIPLOMAT = "diplomat"
    CITIZEN = "citizen"
    ACTIVIST = "activist"
    POLITICIAN = "politician"


class Faction(str, Enum):
    SIDE_A = "side_a"
    SIDE_B = "side_b"
    NEUTRAL = "neutral"


class ChatTurn(BaseModel):
    user: str
    ai: str


class KalkiScore(BaseModel):
    empathy: int
    diplomatic_skill: int
    historical_accuracy: int
    ethical_balance: int
    total_score: int


class ConflictRequest(BaseModel):
    conflict_type: ConflictType
    player_role: Role
    player_faction: Faction
    user_input: str
    current_stage: int = 1
    tension_level: int = 50
    chat_history: List[ChatTurn] = []
    session_id: Optional[str] = None


class ConflictResponse(BaseModel):
    response: str
    tension_level: int
    current_stage: int
    available_actions: List[str]
    is_concluded: bool
    metadata: Dict
    session_id: str
    kalki_score: Optional[KalkiScore] = None