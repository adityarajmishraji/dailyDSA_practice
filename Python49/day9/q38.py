number = int(input("Enter Any natural Number to get no. pattren :"))

for i in range(1, number + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print("")
