# infrastructure/user_repo_impl.py
from domain.entities import User
from interface.user_repository import UserRepository

class InMemoryUserRepository(UserRepository):
    def __init__(self):
        self.users = []
        self.counter = 1

    def create(self, user: User) -> User:
        user.id = self.counter
        self.users.append(user)
        self.counter += 1
        return user

    def get_all(self) -> list[User]:
        return self.users

    def get_by_id(self, user_id: int) -> User | None:
        for user in self.users:
            if user.id == user_id:
                return user
        return None

    def update(self, user_id: int, user: User) -> User | None:
        for i, u in enumerate(self.users):
            if u.id == user_id:
                updated_user = User(id=user_id, name=user.name, email=user.email)
                self.users[i] = updated_user
                return updated_user
        return None

    def delete(self, user_id: int) -> bool:
        for i, u in enumerate(self.users):
            if u.id == user_id:
                del self.users[i]
                return True
        return False


