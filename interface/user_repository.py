# interface/user_repository.py
from abc import ABC, abstractmethod
from domain.entities import User

class UserRepository(ABC):
    @abstractmethod
    def create(self, user: User) -> User: pass

    @abstractmethod
    def get_all(self) -> list[User]: pass

    @abstractmethod
    def get_by_id(self, user_id: int) -> User | None: pass

    @abstractmethod
    def update(self, user_id: int, user: User) -> User | None: pass

    @abstractmethod
    def delete(self, user_id: int) -> bool: pass


