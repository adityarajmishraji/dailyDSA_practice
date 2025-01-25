rows = int(input("Enter Any Number :"))
i = rows
while i >= 1:
    j = rows
    while j > i:
        print(" ", end=" ")
        j -= 1
    k = 1
    while k <= i:
        print("$", end=" ")
        k += 1
    print()
    i -= 1
