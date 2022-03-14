from ujson import load, dump
from http import HTTPStatus
from flask import request
import os

def create_database():
    default_database = {"data": []}

    os.mkdir("app/database")
    os.system("touch app/database/database.json")
    with open(f"./app/database/database.json", "a") as json_file:
        dump(default_database, json_file, indent=2)

def checking_database():
    
    try:
        with open(f"./app/database/database.json", "r") as json_file:
            readable_file = load(json_file)
            return readable_file, HTTPStatus.OK

    except FileNotFoundError:
        create_database()
        with open ("./app/database/database.json", "r") as json_file:
            readable_file = load(json_file)
            return readable_file, HTTPStatus.OK
        

def creating_user():
    users = ""

    try:
        with open("./app/database/database.json", "r") as json_file:
            users = load(json_file)
    except FileNotFoundError:
        create_database()
        with open ("./app/database/database.json", "r") as json_file:
            users = load(json_file)


    name_type = type(request.get_json()["name"])
    email_type = type(request.get_json()["email"])

    if email_type != str and name_type != str:
        return {"Wrong fields": [{"nome": f"{name_type}"}, {"email": f"{email_type}"}]}, HTTPStatus.BAD_REQUEST
    
    elif email_type != str:
        return {"Wrong fields": {"email": f"{email_type}"}}, HTTPStatus.BAD_REQUEST
    
    elif name_type != str:
        return {"Wrong fields": {"nome": f"{name_type}"}}, HTTPStatus.BAD_REQUEST

    input_email = request.get_json()["email"]
    input_name  = request.get_json()["name"]

    email = input_email.lower()
    name = input_name.title()
    id = len(users["data"]) + 1
    
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
    

