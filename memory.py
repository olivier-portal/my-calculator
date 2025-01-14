"""
Authors : Lorenzo OTTAVIANI, Olivier PORTAL et Thibault CARON.
Date : 14/01/2025 09h25
Aim of the program :
    Execute a calculator.
Inputs : Numbers used in the calculator operations.
Output : Details of the operations executed.
"""


def number_input():
    """
    Function used to input a number.
    :return: The number.
    """

    test = False

    while not test:
        number = input("Enter your number: ")
        try:
            number = int(number)
            test = True
        except ValueError:
            try:
                number = float(number)
                test = True
            except ValueError:
                print("Not a number!")

    return number


def calculate(result=None):
    """
    Function used to perform the calculation based on the inputs.
    :return: A tuples of the inputs and the result of the operation.
    """

    if not result:
        number_1 = number_input()
    else:
        number_1 = result

    operation = input("""
    Please type in the math operation you would like to complete:
    +: addition
    -: subtraction
    *: multiplication
    /: division
    **: power
    %: modulo (remainder of division)
    //: floor division
    """)

    number_2 = number_input()

    if operation == "+":
        result = number_1 + number_2
        print(f"{number_1} + {number_2} = ", end="")
        print(result)

    elif operation == "-":
        result = number_1 - number_2
        print(f"{number_1} - {number_2} = ", end="")
        print(result)

    elif operation == "*":
        result = number_1 * number_2
        print(f"{number_1} * {number_2} = ", end="")
        print(result)

    elif operation == "/":
        result = number_1 / number_2
        if result == int(result):
            result = int(result)
        print(f"{number_1} / {number_2} = ", end="")
        print(result)

    elif operation == "**":
        result = number_1 ** number_2
        print(f"{number_1} ** {number_2} = ", end="")
        print(result)
    
    elif operation == "%":
        result = number_1 % number_2
        print(f"{number_1} % {number_2} = ", end="")
        print(result)

    elif operation == "//":
        result = number_1 // number_2
        print(f"{number_1} // {number_2} = ", end="")
        print(result)
    
    else:
        print("You have not typed a valid operator, please run the program again.")

    # Save the operation details in history
    operation_history.append((number_1, operation, number_2, result))

    return number_1, operation, number_2, result

def display_history():
    """
    Function to display the history of operations.
    :return: None
    """
    if not operation_history:
        print("No operations performed yet.")
    else:
        print("\nOperation History:")
        for index, (number_1, operation, number_2, result) in enumerate(operation_history, start=1):
            print(f"{index}. {number_1} {operation} {number_2} = {result}")


def again():
    """
    Function used to provide options to the user to exit, enter a new operation, and use the previous result.
    :return: None
    """
    calc_again = input("""
Do you want to calculate again?
Please type Y for YES or N for NO,
P to start a new calculation using the previous result
""")

    if calc_again.upper() == "Y":
        calculate()
        again()

    elif calc_again.upper() == "P":
        result = operation_history[-1]
        result = result[3]
        print(f"result: {result}")
        calculate(result)

    elif calc_again.upper() == "N":
        display_history()
        print("See you later.")

    else:
        again()


if __name__ == "__main__":  # The program will be run only if executed directly, not if it called from another program.

    operation_history = []

    calculate()
    again()
