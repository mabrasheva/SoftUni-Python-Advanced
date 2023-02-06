from json import dumps, loads

users_file = "./users.txt"


def register(email, password):
    with open(users_file) as users_db:
        for line in users_db:
            user = loads(line.strip())
            if user["email"] == email:
                return False
    with open(users_file, "a") as users_db:
        user = {
            "email": email,
            "password": password,
        }
        user_json = dumps(user)
        users_db.write(user_json + "\n")
        return True


def login(email, password):
    with open(users_file) as users_db:
        for line in users_db:
            user = loads(line.strip())
            if user["email"] == email and user["password"] == password:
                return True
        return False
