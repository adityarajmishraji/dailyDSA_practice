op1 = int(input("Enter First Operand :"))
op2 = int(input("Enter Second Operand :"))
op = input("Enter Operator :")
if op == '+':
    add = op1 + op2
    print("Addition is :",add)
elif op == '-':
    sub = op1 - op2
    print("Subtraction is:",sub)
elif op == '*':
    mul = op1 * op2
    print("Multiplication is :", mul)
elif op == '/':
    if op2 == 0:
        print(" ZeroDivisioError occur!!! \n Please Enter any integer in operand 2 i.e- Denominator except )!!! ")
    else:
        print(op1 / op2)
else:
    print("Enter Proper Operator")
