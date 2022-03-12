
import os
from flask import Flask
from ujson import dump

app = Flask(__name__)

def create_file():
    os.chdir("./database")
    default = {"data": []}
    with open("database.json", "w") as json_file:
        dump(default, json_file, indent=2)

def check_database_dir():
    directories = os.listdir()
    parent_dir = os.getcwd()
    directory = "database"
    path = os.path.join(parent_dir, directory)
    for item in directories:
        if item != directory:
            os.mkdir(path)
            create_file()

@app.get("/user")
def get_users():
    try:
        check_database_dir()
    except FileExistsError:
        return "User"
        # Retornar o que achamos 