# presentation/user_routes.py
from fastapi import APIRouter, HTTPException
from domain.entities import User
from usecases.user_service import UserService
from infrastructure.user_repo_impl import InMemoryUserRepository

repo = InMemoryUserRepository()
service = UserService(repo)

router = APIRouter()

@router.post("/users", response_model=User)
def add_user(user: User):
    return service.create_user(user)

@router.get("/users", response_model=list[User])
def browse_users():
    return service.get_users()

@router.get("/users/{user_id}", response_model=User)
def read_user(user_id: int):
    user = service.get_user(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.put("/users/{user_id}", response_model=User)
def edit_user(user_id: int, user: User):
    updated = service.update_user(user_id, user)
    if not updated:
        raise HTTPException(status_code=404, detail="User not found")
    return updated

@router.delete("/users/{user_id}")
def delete_user(user_id: int):
    success = service.delete_user(user_id)
    if not success:
        raise HTTPException(status_code=404, detail="User not found")
    return {"deleted": True}


