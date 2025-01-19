a = int(input("Enter angle A: "))
b = int(input("Enter angle B: "))
c = int(input("Enter angle C: "))

# Sum of angles in a triangle should be 180 degrees
if a + b + c == 180 and a > 0 and b > 0 and c > 0:
    if a == 90 or b == 90 or c == 90:
        print("Right Angle Triangle")
    elif a < 90 and b < 90 and c < 90:
        print("Acute Angle Triangle")
        if a == b == c:
            print("Equilateral Triangle")
        elif a == b or b == c or c == a:
            print("Isosceles Triangle")
        else:
            print("Scalene Triangle")
    else:
        print("Obtuse Angle Triangle")
else:
    print("Triangle Not Possible")


# Examples for Each Triangle Type
# Right Angle Triangle:

# Example 1: 90, 45, 45

# Example 2: 30, 60, 90

# Example 3: 90, 60, 30

# Acute Angle Triangle:

# Equilateral Triangle:

# Example 1: 60, 60, 60

# Isosceles Triangle:

# Example 1: 70, 70, 40

# Example 2: 50, 50, 80

# Scalene Triangle:

# Example 1: 50, 60, 70

# Example 2: 40, 60, 80

# Obtuse Angle Triangle:

# Example 1: 120, 30, 30

# Example 2: 110, 35, 35

# Example 3: 100, 40, 40

# Invalid Triangle:

# Example 1: 0, 90, 90 (An angle is zero)

# Example 2: 90, 90, 90 (Sum is 270)

# Example 3: 100, 50, 50 (Sum is 200)