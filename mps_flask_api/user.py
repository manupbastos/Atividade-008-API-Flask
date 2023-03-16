from datetime import datetime
from flask import abort, make_response


def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H;%M,%S"))


USER = {
    "1000": {
        "user_name": "Chuu do Loona",
        "user_id": "1000",
        "user_email": "chuudoloona@gmail.com",
        "user_senha":"hihigh",
        "timestamp": get_timestamp()
    },
    "2000": {
        "user_name": "Hanna Montana",
        "user_id": "2000",
        "user_email": "hannamontana@gmail.com",
        "user_senha":"popstar",
        "timestamp": get_timestamp()
    },
    "3000": {
        "user_name": "Dora Aventureira",
        "user_id": "2000",
        "user_email": "doraaventureira@gmail.com",
        "user_senha":"raposo",
        "timestamp": get_timestamp()
    }
}


def read_all():
    return list(USER.values())


def create(user):
    user_id = user.get("user_id")
    user_name = user.get("user_name", "")
    user_email = user.get("user_email", "")
    user_password = user.get("user_password", "")

    if user_id and user_id not in USER:
        USER[user_id] = {
            "user_id": user_id,
            "user_name": user_name,
            "user_email": user_email,
            "user_password": user_password,
            "timestamp": get_timestamp(),
        }
        return USER[user_id], 201
    else:
        abort(
            406,
            f"User with last name {user_id} already exits",
        )


def read_one(user_id):
    if user_id in USER:
        return USER[user_id]
    else:
        abort(
            404, f"Person with ID {user_id} not found"
        )


def update(user_id, user):
    if user_id in USER:
        USER[user_id]["user_name"]= user.get("user_name", USER[user_id]["user_name"])
        USER[user_id]["user_email"] = user.get("user_email", USER[user_id]["user_email"])
        USER[user_id]["user_password"] = user.get("user_password", USER[user_id]["user_password"])
        USER[user_id]["timestamp"] = get_timestamp()
        return USER[user_id]
    else:
        abort(
            404,
            f"Person with ID {user_id} not found"
        )


def delete(user_id):
    if user_id in USER:
        del USER[user_id]
        return make_response(
            f"{user_id} successfully deleted", 200
        )
    else:
        abort(
            404,
            f"Person with ID {user_id} not found"
        )
