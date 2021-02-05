# A simple Calculator made with pure Python 3

# Addition
def add(x, y):
    return x + y

# Subtractio
def subtract(x, y):
    return x - y

# ,ultiplication
def multiply(x, y):
    return x * y

# division
def divide(x, y):
    return x / y


print("Please Select.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:
    choice = input("Enter choice 1, 2 ,3 4, (as a number): ")

    # If Statement
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
        break
    else:
        print("Invalid Input")
