"""
Authors : Lorenzo OTTAVIANI, Olivier PORTAL et Thibault CARON.
Date : 14/01/2025 12h54
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
    act = True

    number_1 = number_input()

    operator = input("""
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

    if operator == "/" or operator == "//":
        if number_2 == 0:
            print("Divide by zero is not allowed!")
            act = False
    elif operator == "**":
        if isinstance(number_2, float):
            print("Exponent must be an integer in power calculation.")
            act = False

    if act is True:
        operation = {"+": number_1 + number_2, "-": number_1 - number_2, "*": number_1 * number_2, "/": number_1 / number_2,
                     "//": number_1 // number_2, "%": number_1 % number_2, "**": number_1 ** number_2}

        for k in operation.keys():
            if k == operator:
                result = operation[k]
                if result == int(result):
                    result = int(result)
                print(f"{number_1} {k} {number_2} = ", end="")
                print(result)


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
