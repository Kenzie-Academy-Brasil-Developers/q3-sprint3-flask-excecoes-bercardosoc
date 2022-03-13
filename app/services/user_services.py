from operator import indexOf
from flask import request
from ujson import load, dump
from http import HTTPStatus
import uuid
import os


def checking_database():
    try:
        os.mkdir("./app/database")
        os.system("touch app/database/database.json")
        with open(f"./app/database/database.json", "a") as json_file:
            json_file.write('{"data": []}')
        with open(f"./app/database/database.json", "r") as json_file:
            readable_file = json_file.read()
        return readable_file, HTTPStatus.OK
    
    except FileExistsError:
        with open(f"./app/database/database.json", "r") as json_file:
            readable_file = json_file.read()
        if readable_file == "":
            with open(f"./app/database/database.json", "a") as json_file:
                json_file.write('{"data": []}')
            with open(f"./app/database/database.json", "r") as json_file:
                readable_file = json_file.read()
                return readable_file, HTTPStatus.OK
        else: 
            with open(f"./app/database/database.json", "r") as json_file:
                readable_file = load(json_file)
                return readable_file, HTTPStatus.OK

def creating_user():
    users = ""

    try:
        with open("./app/database/database.json", "r") as json_file:
            users = load(json_file)
    except FileNotFoundError:
        os.mkdir("app/database")
        os.system("touch app/database/database.json")
        with open(f"./app/database/database.json", "a") as json_file:
            json_file.write("{data: []}")
        with open ("./app/database/database.json", "r") as json_file:
            users = load(json_file)

    if type(request.get_json()["email"]) != str and type(request.get_json()["name"]) != str:
        return {"message": "Wrong fields format"}, HTTPStatus.BAD_REQUEST
    elif type(request.get_json()["email"]) != str:
        return {"message": "Wrong email field format"}, HTTPStatus.BAD_REQUEST
    elif type(request.get_json()["name"]) != str:
        return {"message": "Wrong name field format"}, HTTPStatus.BAD_REQUEST

    input_email = request.get_json()["email"]
    input_name  = request.get_json()["name"]

    email = input_email.lower()
    name = input_name.title()
    id = uuid.uuid1()
    
    user_data = {
        "email": f"{email}",
        "name": f"{name}",
        "id": f"{id}"
    }

    for data in users["data"]:
        if data["email"] == email:
            return {"message": "E-mail already exists"}, HTTPStatus.CONFLICT
    with open("./app/database/database.json", "w") as json_file:
        users["data"].append(user_data)
        dump(users, json_file, indent=2)
        return {
            "data": user_data
        }, HTTPStatus.CREATED
    

