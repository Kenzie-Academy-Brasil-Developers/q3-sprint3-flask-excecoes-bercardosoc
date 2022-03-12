from app.services.json_handler import write_json

class User:
    DATABASE_FILEPATH = "./app/database/database.json"

    def __init__(self, email: str, name: str) -> None:
        self.email: email
        self.name: name

    def create_user(self):
        return write_json(self.DATABASE_FILEPATH, self.__dict__)