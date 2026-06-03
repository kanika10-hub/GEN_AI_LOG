def login_required(func):

    def wrapper(user):

        if not user["authenticated"]:
            print("Access Denied")
            return

        return func(user)

    return wrapper


@login_required
def dashboard(user):

    print(
        f"Welcome {user['name']}"
    )


user1 = {
    "name": "Kanika",
    "authenticated": True
}

user2 = {
    "name": "Guest",
    "authenticated": False
}

dashboard(user1)
dashboard(user2)
