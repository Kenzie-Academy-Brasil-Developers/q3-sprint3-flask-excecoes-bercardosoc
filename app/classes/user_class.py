from app.services.json_handler import read_json, write_json

class User:
    DATABASE_FILEPATH = "./app/database/database.json"

    def __init__(self, email: str, name: str) -> None:
        self.email: email.lower()
        self.name: name.title()
        self.id = len(read_json(self.DATABASE_FILEPATH)["data"]) + 1

    @classmethod
    def get_users(cls):
        return read_json(cls.DATABASE_FILEPATH)

    def create_user(self):
        new_user = self.__dict__
        return write_json(self.DATABASE_FILEPATH, new_user)