# 8. Find the type of user input. 

a = input("Enter any data types: ")
try:
    val = int(a)
    print(f"{val} is a integer value")
except ValueError:
    try:
        val = float(a)
        print(f"{val} is a float value")
    except ValueError:
        if a.lower() == "true":
            print(f"This is a boolean value")
        elif a.lower() == "false":
            print(f"This is a boolean value")
        else:
            print(f"The input is a string. '{a}'")
