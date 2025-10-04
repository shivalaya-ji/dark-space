import pymysql


def authaccount_lookup(session):
    user_id = session["user_id"]
    return get_account(user_id)


#  ********************************************
#  Don't touch anything below this line
#  Utility functions below
#  ********************************************

db = pymysql.connect(
    host="mysql", port=3306, user="root", passwd="letmein", db="BankApp"
)


def get_account(user_id):
    if not user_id:
        return False

    cursor = db.cursor()
    statement = "SELECT balance, dob FROM tbl_account WHERE user_id = %s ;"
    cursor.execute(statement, (str(user_id)))
    data = cursor.fetchone()

    if not data:
        return False

    return {
        "balance": data[0],
        "dob": data[1],
        "username": get_user(user_id)[0],
    }


def user_exists(username):
    user_id = get_user_id(username)

    if not user_id:
        return False

    return True


def user_id_exists(user_id):
    username = get_user(user_id)

    if not username:
        return False

    return True


def get_user_id(username):
    cursor = db.cursor()
    statement = "SELECT id FROM tbl_user WHERE username = %s ;"
    cursor.execute(statement, (username))
    user_id = cursor.fetchone()

    if not user_id:
        return False

    return user_id[0]


def get_user(user_id):
    cursor = db.cursor()
    statement = "SELECT username, role FROM tbl_user WHERE id = %s ;"
    cursor.execute(statement, (user_id))
    user = cursor.fetchone()

    if not user:
        return False

    return user


def authorize(session):
    user_id = session["user_id"]
    decoded_jwt = session["decoded_jwt"]

    username = decoded_jwt["username"]
    role = decoded_jwt["role"]

    current_users_id = get_user_id(username)

    if not user_exists(username):
        return False

    if int(current_users_id) == int(user_id):
        return True

    if not role == "Administrator":
        return False
    return True
