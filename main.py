print("Hello world!")
# name = input("Enter you name: ")

# a=1
# b=3
# print(a+b)

def addition(a,b):
    return a+b
def minus(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    if b == 0:
        return print("Division by 0 is not possible")
    else:
        return a/b


def main():
    print("Select operation")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiplication")
    print("4. Division")

    choice = input("Enter your choice: ")
    if choice in ["1",'2','3','4']:
        x= int(input("Enter first no: "))
        y= int(input("Enter 2nd number: "))
        
        if choice == '1':
            print(addition(x,y))
        elif choice == '2':
            print(minus(x,y))
        elif choice == '3':
            print(multiply(x,y))
        elif choice == '4':
            print(divide(x,y))
        else: print('Invalid input. U DUMB!')

main()