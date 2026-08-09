# 4.	Find the largest of three numbers. 

a = float(input("Enter the 1st number: "))
b = float(input("Enter the 2nd number: "))
c = float(input("Enter the 3rd number: "))

if a == b == c:
    print("All numbers are equal")
elif a >= b and a >= c:
    print(f"The greater number is {a}")
elif b >= a and b >= c:
    print(f"The greater number is {b}")
else:
    print(f"The greater number is {c}")