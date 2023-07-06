from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from services.codeforces.models import Problem


class Duel(BaseModel):
    challengerId: int
    challengeeId: Optional[int] = None
    rating: int
    tag: Optional[str] = None
    acceptedTime: Optional[datetime] = None
    problem: Optional[Problem] = None
