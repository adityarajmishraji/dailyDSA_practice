number = int(input("Enter Any Number"))

for i in range(1, number):
    for j in range(number - 1, 0, -1):
        if j <= i:
            print(j, end=" ")
        else:
            print(" ", end=" ")
    print()
