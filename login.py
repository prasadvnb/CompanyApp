def login():
    print("User login functionality")
login()

 if username == "admin" and password == "admin123":
        print("Login Successful")
    else:
        print("Invalid Credentials")

login("admin", "admin123")

def login(username, password):
    if username.lower() == "admin" and password == "admin123":
        print("Login Successful")
    else:
        print("Invalid Credentials")
