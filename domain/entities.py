# domain/entities.py
from pydantic import BaseModel

class User(BaseModel):
    id: int | None = None
    name: str
    email: str

    def __str__(self):
        return f"User(id={self.id}, name={self.name}, email={self.email})"
