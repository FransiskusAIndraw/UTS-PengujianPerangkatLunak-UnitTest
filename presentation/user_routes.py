from fastapi import APIRouter, HTTPException
from domain.entities import User
from usecases.user_service import UserService
from infrastructure.user_repo_impl import InMemoryUserRepository
from presentation.schemas import UserSchema

repo = InMemoryUserRepository()
service = UserService(repo)

router = APIRouter()

@router.post("/users", response_model=UserSchema)
def add_user(user: UserSchema):
    user_entity = User(id=None, name=user.name, email=user.email)
    created_user = service.create_user(user_entity)
    return UserSchema(**created_user.dict)

@router.get("/users", response_model=list[UserSchema])
def browse_users():
    users = service.get_users()
    return [UserSchema(**u.dict) for u in users]

@router.get("/users/{user_id}", response_model=UserSchema)
def read_user(user_id: int):
    user = service.get_user(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return UserSchema(**user.dict)

@router.put("/users/{user_id}", response_model=UserSchema)
def edit_user(user_id: int, user: UserSchema):
    updated_user = service.update_user(user_id, User(id=user_id, name=user.name, email=user.email))
    if not updated_user:
        raise HTTPException(status_code=404, detail="User not found")
    return UserSchema(**updated_user.dict)

@router.delete("/users/{user_id}")
def delete_user(user_id: int):
    success = service.delete_user(user_id)
    if not success:
        raise HTTPException(status_code=404, detail="User not found")
    return {"deleted": True}