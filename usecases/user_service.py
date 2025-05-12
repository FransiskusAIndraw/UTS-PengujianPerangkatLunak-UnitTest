# usecases/user_service.py
from interface.user_repository import UserRepository
from domain.entities import User

class UserService:
    def __init__(self, repo: UserRepository):
        self.repo = repo

    def create_user(self, user: User) -> User:
        return self.repo.create(user)

    def get_users(self) -> list[User]:
        return self.repo.get_all()

    def get_user(self, user_id: int) -> User | None:
        return self.repo.get_by_id(user_id)

    def update_user(self, user_id: int, user: User) -> User | None:
        return self.repo.update(user_id, user)

    def delete_user(self, user_id: int) -> bool:
        return self.repo.delete(user_id)


