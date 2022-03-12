from flask import Flask

from app.services.user_services import checking_database, creating_user

app = Flask(__name__)

@app.get("/user")
def get_users():

    return checking_database()

@app.post("/user")
def post_user():

    return creating_user()