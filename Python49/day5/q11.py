number = int(input("Enter any number :"))
sum = 0

while(number > 0):
    reminder = number % 10
    sum = sum + reminder
    number = number // 10

print("\n Sum of the digits of given number is =",sum)
