# 2.	Check username and password. 

correct_username = "admin"
correct_password = "Amit@123"

username = input("Enter your username: ")
password = input("Enter your password: ")

if username == correct_username:
    if password == correct_password:
        print("Login successfully")
    else:
        print("Please enter the correct password.")
else:
    print("Please enter the correct username.")   