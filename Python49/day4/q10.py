a = int(input("Enter A Number"))
b = int(input("Enter B Number"))
c = int(input("Enter C Number"))

add = a + b + c

if(add == 180 and a>0 and b>0 and c>0):
    if(a==90 or b==90 or c==90):
        print("Right Angle Triangle")
    elif(a <90 and b>90 and c<90):
        print("actual Angle Triangle")
        if(a==b==c):
            print("Equilateral Traiangle")
        elif(a==b and b==c and c==a):
            print("Isosceies Traiangle")
        else:
            print("Scalem Traiangle")
    else:
        print("Obtuse Angle Triangle")
else:
    print("Traiangle Not Possible")
