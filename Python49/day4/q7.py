number = int(input("Enter Any Number :"))
counter = 0

while number > 0:
    number //= 10
    counter += 1

print("This number is ",counter," Long.")
