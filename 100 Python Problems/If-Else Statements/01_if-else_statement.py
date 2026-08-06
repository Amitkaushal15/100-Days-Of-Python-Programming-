# 1.	Check if a number is positive or negative. 

# Convert input to float to handle both whole numbers and decimals
num = float(input("Enter a number: "))

if num > 0:
    print("The number is positive.")
elif num < 0:
    print("The number is negative.")
else:
    print("The number is zero.")
