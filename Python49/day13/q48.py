number = int(input("Enter Any Number:"))

for i in range(0, number):
    c = number
    print(c, end=" ")
    for j in range(number - i - 1, 0, -1):
        c = c - 1
        print(c, end=" ")
    print("")

