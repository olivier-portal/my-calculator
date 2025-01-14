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
    Function use to input a number.
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


def calculate():

    number_1 = number_input()

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
        print("{} + {} = ".format(number_1, number_2), end="")
        print(result)

    elif operation == "-":
        result = number_1 - number_2
        print("{} - {} = ".format(number_1, number_2), end="")
        print(result)

    elif operation == "*":
        result = number_1 * number_2
        print("{} * {} = ".format(number_1, number_2), end="")
        print(result)

    elif operation == "/":
        result = number_1 / number_2
        if result == int(result):
            result = int(result)
        print("{} / {} = ".format(number_1, number_2), end="")
        print(result)

    elif operation == "**":
        result = number_1 ** number_2
        print("{} ** {} = ".format(number_1, number_2), end="")
        print(result)
    
    elif operation == "%":
        result = number_1 % number_2
        print("{} % {} = ".format(number_1, number_2), end="")
        print(result)

    elif operation == "//":
        result = number_1 // number_2
        print("{} % {} = ".format(number_1, number_2), end="")
        print(result)
    
    else:
        print("You have not typed a valid operator, please run the program again.")


def again():
    calc_again = input("""
Do you want to calculate again?
Please type Y for YES or N for NO.
""")

    if calc_again.upper() == "Y":
        calculate()
        again()
    elif calc_again.upper() == "N":
        print("See you later.")
    else:
        again()


if __name__ == "__main__":  # The program will be run only if executed directly, not if it called from another program.

    calculate()
    again()
