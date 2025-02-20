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

#1. Right Angle Triangle(A right-angled triangle is a type of triangle that has one of its angles equal to 90 degrees. The other two angles sum up to 90 degrees.):

# Example 1: 90, 45, 45

# Example 2: 30, 60, 90

# Example 3: 90, 60, 30

# 2.Acute Angle Triangle( all angle is belongs to 0 degree to 90 degree):

#3. Equilateral Triangle(each angle measure 60 degrees and all its sides equal in length):

# Example 1: 60, 60, 60

#4. Isosceles Triangle( In geometry that has at least two sides of equal length. The angles opposite these sides are also equal.):

# Example 1: 70, 70, 40

# Example 2: 50, 50, 80

#5. Scalene Triangle(A scalene triangle is a triangle in which all three sides are in different lengths, and all three angles are of different measures):

# Example 1: 50, 60, 70

# Example 2: 40, 60, 80

#6. Obtuse Angle Triangle(A triangle whose any one of the angles is an obtuse angle or more than 90°):

# Example 1: 120, 30, 30

# Example 2: 110, 35, 35

# Example 3: 100, 40, 40

#7. Invalid Triangle(A triangle is valid if the sum of the three angles is equal to 180 degree and none of the angle is 0. If any condition disagree the it is invalid triangle):

# Example 1: 0, 90, 90 (An angle is zero)

# Example 2: 90, 90, 90 (Sum is 270)

# Example 3: 100, 50, 50 (Sum is 200)