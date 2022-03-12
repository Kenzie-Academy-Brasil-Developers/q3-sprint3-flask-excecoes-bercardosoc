from http import HTTPStatus
from flask import Flask, jsonify, request
from app.classes.user_class import User
app = Flask(__name__)

DATABASE_FILEPATH = "database/database.json"

@app.get("/user")
def get_users():
    return jsonify(User.get_users()), HTTPStatus.OK

@app.post("/user")
def creating_user():

    # data = request.get_json()
    # user = User(**data)     
    new_user = User(**request.get_json())
    return new_user.create_user(), HTTPStatus.CREATED
    