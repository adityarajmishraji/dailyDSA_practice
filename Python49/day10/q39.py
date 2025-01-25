number = int(input("Enter Any Number :"))

for i in range(1, number):
    num = 1

    for j in range(number, 0, -1):
        if j > i:
            print(" ", end=" ")
        else:
            print(num, end=" ")
            num = num + 1
    print("")
