def is_even(i):
    if i % 2 == 0:
        return "Even"
    else:
        return "Odd"

i = int(input("Enter the number: "))
print(is_even(i))