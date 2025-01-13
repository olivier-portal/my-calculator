"""
Authors : Lorenzo OTTAVIANI, Olivier PORTAL et Thibault CARON.
Date : 13/01/2025 15h03
Aim of the program :
    Execute a calculator.
Inputs : Numbers used in the calculator operations.
Output : Details of the operations executed.
"""


def calculate():

    number_1 = float(input("Please enter the first number: "))
    if number_1 == int(number_1):
        number_1 = int(number_1)

    operation = input('''
    Please type in the math operation you would like to complete:
    +: addition
    -: subtraction
    *: multiplication
    /: division
    **: power
    %: modulo
    //: floor division
    ''')

    number_2 = int(input("Please enter the second number: "))
    if number_2 == int(number_2):
        number_2 = int(number_2)

    if operation == '+':
        result = number_1 + number_2
        print('{} + {} = '.format(number_1, number_2), end="")
        print(result)

    elif operation == '-':
        result = number_1 - number_2
        print('{} - {} = '.format(number_1, number_2), end="")
        print(result)

    elif operation == '*':
        result = number_1 * number_2
        print('{} * {} = '.format(number_1, number_2), end="")
        print(result)

    elif operation == '/':
        result = number_1 / number_2
        print('{} / {} = '.format(number_1, number_2), end="")
        print(result)

    elif operation == '**':
        result = number_1 ** number_2
        print('{} ** {} = '.format(number_1, number_2), end="")
        print(result)
    
    elif operation == '%':
        result = number_1 % number_2
        print('{} % {} = '.format(number_1, number_2), end="")
        print(result)

    elif operation == '//':
        result = number_1 // number_2
        print('{} % {} = '.format(number_1, number_2), end="")
        print(result)
    
    else:
        print("You have not typed a valid operator, please run the program again.")


def again():
    calc_again = input('''
Do you want to calculate again?
Please type Y for YES or N for NO.
''')

    if calc_again.upper() == 'Y':
        calculate()
        again()
    elif calc_again.upper() == 'N':
        print("See you later.")
    else:
        again()


if __name__ == "__main__":  # The program will be run only if executed directly, not if it called from another program.
    calculate()
    again()
