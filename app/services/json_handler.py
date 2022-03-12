from json import JSONDecodeError
import os
import ujson as json
from ujson import dump

def create_file():
    default = {"data": []}
    with open("database/database.json", "w") as json_file:
        dump(default, json_file, indent=2)

def check_database_dir():
        os.chdir("./app")
        directories = os.listdir()
        parent_dir = os.getcwd()
        directory = "database"
        path = os.path.join(parent_dir, directory)
        for item in directories:
            if item != directory:
                os.mkdir(path)
                create_file()

def read_json(database) -> list:
    try:
        with open(database, "r") as json_file:
            dados = json.load(json_file)
            return dados
    except (FileNotFoundError, JSONDecodeError):
        return []

def write_json(database: list, payload: dict):
    json_list = list(read_json(database))
    json_list.append(payload)
 
    with open(database, "w") as json_file:
        json.dump(json_list, json_file, indent=2)

        return payload