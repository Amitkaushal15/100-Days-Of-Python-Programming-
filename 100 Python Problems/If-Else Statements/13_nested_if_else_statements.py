# 3. Create a Python program that takes a student's Class 12 percentage, entrance exam score, and age, and checks whether the student is eligible for college admission.

percentage = float(input("Enter Class 12 percentage: "))
entrance_score = float(input("Enter entrance exam score: "))
age = int(input("Enter age: "))

if percentage >= 60 and entrance_score >= 50 and age >= 17:
    print("Eligible for admission")
else:
    print("Not eligible for admission")
