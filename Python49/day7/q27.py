number = int(input("Enter any number ;"))

total = 0
count = 0

for i in range(1, number+1):
        if(i % 2 == 0):
                print(i)
                total = total + i
                count = count + 1
                
avg = total / count

print("Sum of the First Natural number is",total)
print("average of Even number is :",avg)

