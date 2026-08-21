# 4.	Compare three numbers using nested if. 

a = float(input("Enter the first number: "))
b = float(input("Enter the 2nd number: "))
c = float(input("Enter the 3rd number: "))

if a >= b:
    if a >= c:
        larger = a
    else:
        larger = c
else:
    if b >= c:
        larger = b
    else:
        larger = c
print(f"The largest number is {larger}")
      
