num = int(input("Enter Number :"))
res = 1

for i in range(1,num + 1):
    if not (i % 2):
        res += i ** 2
    else:
        res -= i ** 2

print("Total :", res)
