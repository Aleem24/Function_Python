# Program for a simple calculator using function
# A function for addition

def add(n1,n2):
    return n1+n2 

def subtract(n1,n2):
    if(n1>n2):
        return n1-n2
    else:
        return n2-n1

def multi(n1,n2):
    return n1*n2

def division(n1,n2):
    return n1/n2

def remainder(n1,n2):
    return n1%n2

def simpleCalculator():
    num1 = int(input("Enter your first number:"))
    num2 = int(input("Enter your second number:"))
    print(f"The addition of {num1} and {num2} is {add(num1,num2)}") 

    print(f"The subtraction of {num1} and {num2} is {subtract(num1,num2)}") 

    print(f"The multiplication of {num1} and {num2} is {multi(num1,num2)}") 

    print(f"The division of {num1} and {num2} is {division(num1,num2)}") 

    print(f"The remainder of {num1} and {num2} is {remainder(num1,num2)}") 

simpleCalculator()