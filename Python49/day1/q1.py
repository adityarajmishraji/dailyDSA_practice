num1 = float(input("Enter your First number : "))
num2 = float(input("Enter your Second number : "))
# for addition
sum_result = num1 + num2
print(f"sum : {num1} + {num2} = {sum_result}")

#for subtraction
sub_result = num1 - num2
print(f"subtract : {num1} - {num2} = {sub_result}")

#for Multiplication
product_result = num1 * num2
print(f"Multiplication : {num1} * {num2} = {product_result}")

# for Division
# div_result = num1 / num2
# print(f"subtract : {num1} / {num2} = {div_result}")

# OR we show the logical error(ZeroDivisionError) i.e- We have shows error on divisible of 0.

if num2 == 0:
    print("Please use integer values except 0 in Denominator!!!")
else:
    print(num1 / num2)

a = int(input("Enter the value of a : "))
b = int(input("Enter the value of b : "))

#for Modules
mod_result = a // b
print(f"Modules : {a} // {b} = {mod_result}")


