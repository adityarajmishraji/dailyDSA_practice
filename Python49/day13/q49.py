number = int(input("Enter Any Number:"))

for i in range(0,number):
    c = 1
    print(" "*(number+i)*2,end=" ")
    for j in range(number-1):
        c = c + 1
        print(c, end=" ")
    print("")
