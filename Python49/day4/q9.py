n1 = int(input("Enter First Number :"))
n2 = int(input("Enter Second Number :"))
n3 = int(input("Enter Third Number :"))

if n1 > n2 and n1 > n3:
    print("First Number is Maximum")
elif n2 > n1 and n2 > n3:
    print("Second Number is Maximum")
elif n3 > n1 and n3 > n2:
    print("Third Number is Maximum")
else:
    print("some are same or all number is zero")
