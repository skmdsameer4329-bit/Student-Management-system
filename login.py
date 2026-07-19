USERNAME = "admin"
PASSWORD = "admin123"

def login():
    print("===== Student Management System Login =====")

    username = input("Username: ")
    password = input("Password: ")

    if username == USERNAME and password == PASSWORD:
        print("Login Successful!")
        return True
    else:
        print("Invalid Username or Password!")
        return False
