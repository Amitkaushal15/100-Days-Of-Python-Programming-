# 1.	Check age and citizenship for voting. 

age = int(input("Enter your age: "))
citizenship = input("Are you a citizen? (yes/no): ").strip().lower()

if age >= 18:
    if citizenship == "yes":
        print("You are eligible to vote.")
    else:
        print("You must be a citizen to vote.")
else:
    print("You must be at least 18 years old to vote.")