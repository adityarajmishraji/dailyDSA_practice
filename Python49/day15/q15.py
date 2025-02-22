# swap two variables

a = input("Enter the value of the first variable (a):")
b = input("Enter the value of the first variable (b):")

print(f"original value : a = {a} , b = {b} ")
temp = a
a = b
b = temp

print(f"Swaped value : a = {a} , b = {b} ")
