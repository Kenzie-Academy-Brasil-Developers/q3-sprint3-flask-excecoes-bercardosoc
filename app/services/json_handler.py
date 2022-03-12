from json import JSONDecodeError
import os
import ujson as json
from ujson import dump

""" def create_file():
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
                create_file() """

def read_json(database) -> list:
    try:
        with open(database, "r") as json_file:
            data = json.load(json_file)
            return data
    except:
        new_data = {"data": []}
        with open(database, "w") as json_file:
            dump(new_data, json_file, indent=2)
        return new_data

def write_json(database, payload):
    
    try:
        json_list = read_json(database)["data"]
        json_list.append(payload)
 
        with open(database, "w") as json_file:
            dump({"data": json_list}, json_file, indent=2)
        return payload

    except:
        with open(database, "w") as json_file:
            dump({"data": [payload]}, json_file, indent=2)
        return payload
