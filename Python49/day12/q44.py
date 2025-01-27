# Right-Angled Triangle with Descending Numbers and Increasing Indentation
number = int(input("Enter Any Number: "))

for i in range(1, number + 1):
    # Print spaces for indentation
    print("  " * (i - 1), end="")

    # Print numbers in descending order
    for k in range(number, 0, -1):
        print(k, end=" ")

    print()  # Move to the next line

