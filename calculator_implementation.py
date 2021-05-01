"""
Project implementation of Digital Calculator
"""
import math


def add(number_1, number_2):

    """
    Takes in two number number_1 and number_2
    returns the addition of number_1 and number_2
    """
    return number_1 + number_2


def subtract(number_1, number_2):
    """
    Takes in two number number_1 and number_2
    returns the subtraction of number_1 and number_2
    """
    return number_1 - number_2


def multiply(number_1, number_2):
    """
    Takes in two number number_1 and number_2
    returns the multiplication of number_1 and number_2
    """
    return number_1 * number_2


def divide(number_1, number_2):
    """
    Takes in two number number_1 and number_2
    returns the division of number_1 and number_2
    """
    try:
        result = number_1/number_2
        return result
    except ZeroDivisionError as exp:
        print("can't divide by zero")
        print(exp)
        return -1


def modulus(number_1, number_2):
    """
    Takes in two number number_1 and number_2
     returns the modulus of number_1 and number_2
    """
    try:
        return number_1 % number_2
    except ValueError as exp:
        print("Can't be Decimal or Negative value")
        print(exp)
        return -1


def exponential(number_1, number_2):
    """
    Takes in two number number_1 and number_2
     returns the exponential of number_1 and number_2
    """
    return pow(number_1, number_2)


def square(number):
    """
    Takes in a number as number
    returns the square of number
    """
    return number**2


def cube(number):
    """
    Takes in a number as number
    returns the cube of number
    """
    return number**3


def cube_root(number):
    """
    Takes in a number as number
    returns the cube_root of number
    """
    return number**(1/3)


def inverse(number):
    """
    Takes in a number as number
    returns the inverse of number
    """
    return 1/number


def factorial(number):
    """
    Takes in a number as number
    returns the factorial of number
    """
    try:
        return math.factorial(number)
    except ValueError as exp:
        print("Can't be Decimal or Negative value")
        print(exp)
        return -1


def simple_interest(principal, time, rate):
    """
    Takes in three number principal, time and rate
    returns the simple_interest
    """
    return (principal * time * rate) / 100


def compound_interest(principal, time, rate):
    """
    Takes in three number principal, time and rate
    returns the compound_interest
    """
    return principal * ((1 + rate / 100) ** time - 1)


def sin_operation():
    """
    Written for sine function
    """
    print("---Two Choices---")
    print("1.Sine of different values")
    print("2.Sine of different degrees")
    choice = input("Enter choice(1/2): ")
    num = float(input("Enter the number: "))
    if choice == '1':
        print(math.sin(num))
    elif choice == '2':
        print(math.sin(math.radians(num)))


def cos_operation():
    """
    Written for cosine function
    """
    print("---Two Choices---")
    print("1.Cosine of different values")
    print("2.Cosine of different degrees")
    choice = input("Enter choice(1/2): ")
    num = float(input("Enter the number: "))
    if choice == '1':
        print(math.cos(num))
    elif choice == '2':
        print(math.cos(math.radians(num)))


def tan_operation():
    """
    Written for tan function
    """
    print("---Two Choices---")
    print("1.Tan of different values")
    print("2.Tan of different degrees")
    choice = input("Enter choice(1/2): ")
    num = float(input("Enter the number: "))
    if choice == '1':
        print(math.tan(num))
    elif choice == '2':
        print(math.tan(math.radians(num)))


def tan_h_operation():
    """
    Written for tan_h function
    """
    num = float(input("Enter the number: "))
    try:
        return math.atanh(num)
    except ValueError as exp:
        print(exp)
        print("Please Enter smaller value between 0 to 1")
        return -1


def basic_operation():
    """
    Calling of add(), subtract(), multiply() and divide()
    """
    print("------Welcome to Basic Operation-------")
    print("--Select Options for operations--")
    print("1.Addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Division")
    choice = input("Enter choice(1/2/3/4): ")
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        if choice == '1':
            print("Addition is:", add(num1, num2))
        elif choice == '2':
            print("Subtraction is:", subtract(num1, num2))
        elif choice == '3':
            print("Multiplication is:", multiply(num1, num2))
        elif choice == '4':
            print("Division is:", divide(num1, num2))
    else:
        print("Invalid Input")


def scientific_operation():
    """
    Calling of modulus(), exponential(), logarithm(), square(),
    square_root(), cube(), cube_root(), factorial() and inverse()
    """
    print("------Welcome to Scientific Operation-------")
    print("--Select Options for operations--")
    print("1.Modulus")
    print("2.Exponential")
    print("3.Logarithm-10")
    print("4.Logarithm-2")
    print("5.Square")
    print("6.Square-root")
    print("7.Cube")
    print("8.Cube-root")
    print("9.Factorial")
    print("10.Inverse")
    choice = input("Enter choice(1/2/3/4/5/6/7/8/9/10): ")
    if choice == '1':
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print("Modulus = ", modulus(num1, num2))
    elif choice == '2':
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print("Exponential = ", exponential(num1, num2))
    elif choice == '3':
        num = float(input("Enter the number: "))
        print("Logarithm-10 = ", math.log10(num))
    elif choice == '4':
        num = float(input("Enter the number: "))
        print("Logarithm-2 = ", math.log2(num))
    elif choice == '5':
        num = float(input("Enter the number: "))
        print("Square = ", square(num))
    elif choice == '6':
        num = float(input("Enter the number: "))
        print("Square_root = ", math.sqrt(num))
    elif choice == '7':
        num = float(input("Enter the number: "))
        print("Cube = ", cube(num))
    elif choice == '8':
        num = float(input("Enter the number: "))
        print("Cube_root = ", cube_root(num))
    elif choice == '10':
        num = float(input("Enter the number: "))
        print("Inverse = ", inverse(num))
    elif choice == '9':
        num = float(input("Enter the number: "))
        print("Factorial is:", factorial(num))
    else:
        print("Invalid Input")


def trigonometric_operation():
    """
    Calling of sin(), cos(), tan(), a_sin_h(), a_cos_h() and a_tan_h()
    """
    print("------Welcome to Scientific Operation-------")
    print("--Select Options for operations--")
    print("1.Sin")
    print("2.Sin_h")
    print("3.Cos")
    print("4.Cos_h")
    print("5.Tan")
    print("6.Tan_h")
    choice = input("Enter choice(1/2/3/4/5/6): ")
    if choice == '1':
        sin_operation()
    elif choice == '2':
        num = float(input("Enter the number: "))
        print(math.asinh(num))
    elif choice == '3':
        cos_operation()
    elif choice == '4':
        num = float(input("Enter the number: "))
        print(math.acosh(num))
    elif choice == '5':
        tan_operation()
    elif choice == '6':
        print(tan_h_operation())
    else:
        print("Invalid Input")


def financial_operation():
    """
    Calling of simple_interest() and compound_interest()
    """
    print("------Welcome to Financial Operation-------")
    print("--Select Options for operations--")
    print("1.Simple-Interest")
    print("2.Compound-Interest")
    choice = input("Enter choice(1/2): ")
    principal = float(input('Enter amount: '))
    time = float(input('Enter time: '))
    rate = float(input('Enter rate: '))
    if choice == '1':
        print("Simple Interest is:", simple_interest(principal, time, rate))
    elif choice == '2':
        print("Compound Interest is:", compound_interest(principal, time, rate))
    else:
        print("Invalid Input")


def main():
    """
    Calling of basic_operation(), scientific_operation(),
    trigonometric_operation() and financial_operation()
    """
    print("------WELCOME TO DIGITAL CALCULATOR-------")
    print("--Select Options for operations--")
    print("1.Basic Operation")
    print("2.Scientific Operation")
    print("3.Trigonometric Operation")
    print("4.Financial Operation")
    choice = input("Enter choice(1/2/3/4):")
    if choice in ('1', '2', '3', '4'):
        if choice == '1':
            basic_operation()
        elif choice == '2':
            scientific_operation()
        elif choice == '3':
            trigonometric_operation()
        elif choice == '4':
            financial_operation()
    else:
        print("Invalid Input")


if __name__ == "__main__":
    main()
