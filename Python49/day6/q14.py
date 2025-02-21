num = int(input("Enter Number :"))
res = 1

for i in range(1,num + 1):
    if not (i % 2):
        res += i ** 2
    else:
        res -= i ** 2

print("Total :", res)

# i	Even/Odd	Operation	Result (res)
# 1	Odd	        res - (1^2)	1 - 1 = 0
# 2	Even	     + (2^2)	0 + 4 = 4
# 3	Odd	res - (3^2)	4 - 9 = -5
# 4	Even	res + (4^2)	-5 + 16 = 11
# 5	Odd	res - (5^2)	11 - 25 = -14

