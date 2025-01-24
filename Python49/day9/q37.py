number = int(input("Enter Number of Rows :"))

for i in range(number):
    for j in range(1, number - i):
        print(" ",end="")
    for k in range(0, i + 1):
        print("*", end="")
    print()
