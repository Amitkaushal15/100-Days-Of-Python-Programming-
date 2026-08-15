# Grade students based on marks.

marks = int(input("Enter your marks: "))

if marks < 0 or marks > 100:
    print("Please enter your marks between 0 to 100.")
elif marks >= 90:
    print("Grade A")
elif marks >= 80:
    print("Grade B")
elif marks >= 70:
    print("Grade C")
elif marks >= 60:
    print("Grade D")
else:
    print("Fail")