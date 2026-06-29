# 6. Count Digits
# Take a number from the user and count how many digits it contains using a loop.

n = int(input("Enter the number: "))
count = 0
while n>0:
    count += 1
    n = n//10
print(count)