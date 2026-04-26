from pydantic import BaseModel

class UserProfile(BaseModel):
    matematica: int
    pratico: int
    tempo: str