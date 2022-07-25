
from art_calculator import logo

def add (n1, n2):
    return n1+ n2

def subtract (n1, n2):
    return n1 - n2

def multiply (n1, n2):
    return n1 * n2

def divide (n1, n2):
    return n1 / n2

operations = {

    "+" : add ,
    "-" : subtract ,
    "*" : multiply,
    "/" : divide,
}

def calculator():

    print(logo)

    num1= float (input("What is the first number ? "))

    for operater in operations:
        print (operater)

    should_continue = True 
    while should_continue:
        operation_symbol= input("Choose an operation: ")
        num2= float (input("What is the next number ? "))
        calculation_fun = operations[operation_symbol]
        answer = calculation_fun (num1, num2)
        print (f"{num1} {operation_symbol} {num2} = {answer}")

        if input(f"Type 'y' if you want to continue calculating with {answer} or type 'n' to start a new: ") == "y" :
            num1 = answer
        else:
            should_continue = False
            calculator()

calculator()




