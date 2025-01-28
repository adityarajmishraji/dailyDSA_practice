num = int(input("Enter Number :"))

for i in range(num, 1, -1):
    for j in range(i-num, 0):
        print(" ", end=" ")
    for k in range(1,i):
        print(k,end=" ")
    print()
