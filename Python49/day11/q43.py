number = int(input("Enter Any Number :"))

for i in range(1,number+1):
    print()
    
    for j in range(i-1):
        print(" ", end=" ")

    
    for k in range(number, 0, -1):
        print(k, end=" ")
    number = number - 1
    
