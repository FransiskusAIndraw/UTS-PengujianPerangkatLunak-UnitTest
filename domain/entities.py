class User:
    def __init__(self, id: int | None = None, name: str = "", email: str = ""):
        self.id = id
        self.name = name
        self.email = email

    def __str__(self):
        return f"User(id={self.id}, name={self.name}, email={self.email})"