# 3. Multiplication Table
# Write a program to print the multiplication table of a number entered by the user.


n = int(input("Enter the number: "))

for i in range(1,11):
    m = n*i
    print(m)