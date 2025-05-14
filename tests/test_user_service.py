import unittest
from usecases.user_service import UserService
from infrastructure.user_repo_impl import InMemoryUserRepository
from domain.entities import User

class TestUserService(unittest.TestCase):
    def setUp(self):
        self.repo = InMemoryUserRepository()
        self.service = UserService(self.repo)

    def test_add_user(self):
        user = User(id=0, name="David", email="david@example.com")
        created = self.service.create_user(user)
        self.assertEqual(created.id, 1)

    def test_get_all_users(self):
        self.service.create_user(User(id=0, name="Eve", email="eve@example.com"))
        users = self.service.get_users()
        self.assertEqual(len(users), 1)

    def test_get_user_by_id(self):
        user = self.service.create_user(User(id=0, name="Frank", email="frank@example.com"))
        fetched = self.service.get_user(user.id)
        self.assertEqual(fetched.name, "Frank")

    def test_update_user_success(self):
        created = self.service.create_user(User(id=0, name="Updatable", email="up@example.com"))
        updated = self.service.update_user(created.id, User(id=0, name="Updated", email="upd@example.com"))
        self.assertEqual(updated.name, "Updated")

    def test_delete_user_success(self):
        created = self.service.create_user(User(id=0, name="ToDelete", email="del@example.com"))
        result = self.service.delete_user(created.id)
        self.assertTrue(result)