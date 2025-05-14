import unittest
from infrastructure.user_repo_impl import InMemoryUserRepository
from domain.entities import User

class TestInMemoryUserRepository(unittest.TestCase):
    def setUp(self):
        self.repo = InMemoryUserRepository()

    def test_create_user(self):
        user = self.repo.create(User(id=0, name="Gina", email="gina@example.com"))
        self.assertEqual(user.id, 1)

    def test_update_user(self):
        user = self.repo.create(User(id=0, name="Hank", email="hank@example.com"))
        updated = self.repo.update(user.id, User(id=0, name="Hank2", email="h2@example.com"))
        self.assertEqual(updated.name, "Hank2")

    def test_delete_user(self):
        user = self.repo.create(User(id=0, name="Ian", email="ian@example.com"))
        result = self.repo.delete(user.id)
        self.assertTrue(result)

    def test_update_nonexistent_user(self):
        updated = self.repo.update(999, User(id=999, name="X", email="x@example.com"))
        self.assertIsNone(updated)

    def test_delete_nonexistent_user(self):
        result = self.repo.delete(12345)
        self.assertFalse(result)