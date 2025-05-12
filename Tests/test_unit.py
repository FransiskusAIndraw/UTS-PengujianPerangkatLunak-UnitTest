
import unittest
from domain.entities import User
from usecases.user_service import UserUseCase

class TestUserUseCase(unittest.TestCase):
    def setUp(self):
        self.usecase = UserUseCase()

    def test_add_user_success(self):
        user = User(id=1, name="Indra", email="indra@example.com")
        result = self.usecase.add_user(user)
        self.assertEqual(result.name, "Indra")
        self.assertEqual(result.email, "indra@example.com")

    def test_add_user_duplicate(self):
        user1 = User(id=1, name="Indra", email="indra@example.com")
        user2 = User(id=1, name="Duplicate", email="dup@example.com")
        self.usecase.add_user(user1)
        with self.assertRaises(ValueError):
            self.usecase.add_user(user2)

    def test_get_user_success(self):
        user = User(id=2, name="Budi", email="budi@example.com")
        self.usecase.add_user(user)
        result = self.usecase.get_user(2)
        self.assertEqual(result.name, "Budi")

    def test_get_user_not_found(self):
        result = self.usecase.get_user(999)
        self.assertIsNone(result)

    def test_update_user_success(self):
        user = User(id=3, name="Sari", email="sari@example.com")
        self.usecase.add_user(user)
        updated = User(id=3, name="Sari Updated", email="sari.new@example.com")
        result = self.usecase.update_user(3, updated)
        self.assertEqual(result.name, "Sari Updated")

    def test_update_user_not_found(self):
        updated = User(id=4, name="NonExistent", email="no@example.com")
        result = self.usecase.update_user(4, updated)
        self.assertIsNone(result)

    def test_delete_user_success(self):
        user = User(id=5, name="ToDelete", email="delete@example.com")
        self.usecase.add_user(user)
        result = self.usecase.delete_user(5)
        self.assertTrue(result)

    def test_delete_user_not_found(self):
        result = self.usecase.delete_user(999)
        self.assertFalse(result)

if __name__ == "__main__":
    unittest.main()
