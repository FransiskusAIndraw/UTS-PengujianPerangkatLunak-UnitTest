import unittest
from domain.entities import User

class TestUserEntity(unittest.TestCase):
    def test_create_user(self):
        user = User(id=1, name="Alice", email="alice@example.com")
        self.assertEqual(user.name, "Alice")
        self.assertEqual(user.email, "alice@example.com")

    def test_user_id_is_set(self):
        user = User(id=5, name="Bob", email="bob@example.com")
        self.assertEqual(user.id, 5)

    def test_user_string_representation(self):
        user = User(id=1, name="Charlie", email="charlie@example.com")
        self.assertTrue(str(user).startswith("User"))
        
    def test_user_fields_assignment(self):
        user = User(id=1, name="Alice", email="alice@example.com")
        self.assertEqual(user.name, "Alice")
        self.assertEqual(user.email, "alice@example.com")

    def test_user_str_representation_format(self):
        user = User(id=2, name="Bob", email="bob@example.com")
        expected = "User(id=2, name=Bob, email=bob@example.com)"
        self.assertEqual(str(user), expected)