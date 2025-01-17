pri = int(input("Enter Principle Amount :"))
rate = int(input("Enter Rate of Interest :"))
num_year = int(input("Enter Number of Year :"))

sim_int = (pri*rate*num_year)//100

# here I add "//" insted of using "/" because we don't need any floating value as a result

print("Simple interest is :",sim_int)
