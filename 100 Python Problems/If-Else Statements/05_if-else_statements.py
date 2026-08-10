# 5.	Check voting eligibility. 

age = int(input("Enter the age: "))

if age < 0:
    print("Age cannot be negative. Please enter a valid age.")
elif age >=18:
    print("You are eligible to vote.")
else:
    print("you are not eligible to vote.")