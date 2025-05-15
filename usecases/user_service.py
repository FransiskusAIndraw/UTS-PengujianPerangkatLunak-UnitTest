import logging
from domain.entities import User
from interface.user_repository import UserRepository

logger = logging.getLogger(__name__)

class UserService:
    def __init__(self, user_repo: UserRepository):
        self.user_repo = user_repo

    def create_user(self, user: User) -> User:
        created = self.user_repo.create(user)
        logger.info(f"[CREATE] User ditambahkan: ID={created.id}, Name={created.name}, Email={created.email}")
        return created

    def get_users(self) -> list[User]:
        users = self.user_repo.get_all()
        logger.info(f"[READ ALL] Total user: {len(users)}")
        return users

    def get_user(self, user_id: int) -> User | None:
        user = self.user_repo.get_by_id(user_id)
        if user:
            logger.info(f"[READ] User ditemukan: ID={user.id}")
        else:
            logger.warning(f"[READ] User dengan ID={user_id} tidak ditemukan")
        return user

    def update_user(self, user_id: int, user: User) -> User | None:
        updated = self.user_repo.update(user_id, user)
        if updated:
            logger.info(f"[UPDATE] User ID={user_id} diupdate: name={user.name}, email={user.email}")
        else:
            logger.warning(f"[UPDATE] Gagal update user ID={user_id} (tidak ditemukan)")
        return updated

    def delete_user(self, user_id: int) -> bool:
        result = self.user_repo.delete(user_id)
        if result:
            logger.info(f"[DELETE] User dengan ID={user_id} berhasil dihapus")
        else:
            logger.warning(f"[DELETE] Gagal menghapus user dengan ID={user_id} (tidak ditemukan)")
        return result
