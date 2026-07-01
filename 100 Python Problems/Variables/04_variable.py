# 4.	Swap two variables without using a third variable. 

num1 = 10
num2 = 20
num1,num2 = num2, num1
print(f"num1: {num1} and num2: {num2}")

#	Swap two variables 

a = 10
b = 20

a = a+b
b = a-b
a = a-b
print(f"a: {a}, b: {b}")