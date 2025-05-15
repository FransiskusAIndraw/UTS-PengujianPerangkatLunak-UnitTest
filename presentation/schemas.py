from pydantic import BaseModel

class UserSchema(BaseModel):
    id: int | None = None
    name: str
    email: str