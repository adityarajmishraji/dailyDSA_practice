number = int(input("Enter Number of Rows"))

for i in range(number + 1, 0, -1):
    for j in range(0, i - 1):
        print("$", end=" ")
    print(" ")
