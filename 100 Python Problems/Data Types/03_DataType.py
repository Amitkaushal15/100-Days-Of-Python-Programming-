# 3.	Convert string to integer. 

x = "12345690"
y = int(x)
print(y)


user_input = "Amit Kaushal"

try:
    number = int(user_input)
    print(f"Success: {number}")
except ValueError:
    print("Error: The string contains non-numeric characters.")