from http import HTTPStatus
from flask import Flask, jsonify, request
from app.services.json_handler import check_database_dir, read_json
from app.classes.user_class import User
app = Flask(__name__)

DATABASE_FILEPATH = "database/database.json"

@app.get("/user")
def get_users():
    try:
        check_database_dir()
    except FileExistsError:
        return jsonify(read_json(DATABASE_FILEPATH))

@app.post("/user")
def creating_user():

    data = request.get_json()
    
    user = User(**data)     
    user.create_user()
    return {"message": "User created"}, HTTPStatus.CREATED
    