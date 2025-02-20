number = int(input("Enter any number: "))
sum = 0

while True:
    reminder = number % 10
    sum = sum + reminder
    number = number // 10
    if number <= 0:
        break

print("\n Sum of the digits of given number is =", sum)
