import math
def areaOfSquare(l):
    print (l*l)
def areaOfCircle(r):
    print(math.pi*r*r)
def areaOfRectangle(g,h):
    print(g*h)
def areaOfEllipse(a,b):
    print(math.pi*a*b)
def areaOFAnnulus(R,r):
    if(R<r):
        print("Outer radius must be greater than or equal to inner radius.")
    else:
        print(math.pi*((R*R)-(r*r)))

def main():
    print("Select The shape whose area needs to be calculated: ")
    print("1. Square")
    print("2. Circle")
    print("3. Rectangle")
    print("4. Ellipse")
    print("5. Annulus")

    choice = input("Enter your choice: ")
    if choice in ["1",'2','3','4','5']:
        if choice == '1':
            u = int(input("Enter length of square: "))
            return areaOfSquare(u)
        elif choice == '2':
            y = int(input("Enter radius of circle: "))
            return areaOfCircle(y)
        elif choice == '3':
            w = int(input("Enter the length of Rectangle: "))
            z = int(input("Enter the width of Rectangle: "))
            return areaOfRectangle(w,z)
        elif choice == '4':
            c = int(input('Enter the semi-major axis: '))
            d = int(input("Enter the semi-minor axis: "))
            return areaOfEllipse(c,d)
        elif choice == '5':
            e = int(input("Enter the outer radius: "))
            t = int(input("Enter the inner radius: "))
            return areaOFAnnulus(e,t)
        else:
            print("Invalid Input")

main()




# Program to find the largest number among three numbers 
def find_largest(a, b, c):
    if a >= b and a >= c:
        largest = a
    elif b >= a and b >= c:
        largest = b
    else:
        largest = c
    return largest

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

largest_number = find_largest(num1, num2, num3)

print("The largest number is:", largest_number)