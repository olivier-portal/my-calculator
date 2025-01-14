from .get_number import get_number
from .get_operator import get_operator

def calculate():
    number_1 = get_number()
    operator = get_operator()
    number_2 = get_number()
    if operator == "+":
        result = number_1 + number_2
        print("{} + {} = ".format(number_1, number_2), end="")
        print(result)

    elif operator == "-":
        result = number_1 - number_2
        print("{} - {} = ".format(number_1, number_2), end="")
        print(result)

    elif operator == "*":
        result = number_1 * number_2
        print("{} * {} = ".format(number_1, number_2), end="")
        print(result)

    elif operator == "/":
        result = number_1 / number_2
        if result == int(result):
            result = int(result)
        print("{} / {} = ".format(number_1, number_2), end="")
        print(result)

    elif operator == "**":
        result = number_1 ** number_2
        print("{} ** {} = ".format(number_1, number_2), end="")
        print(result)
    
    elif operator == "%":
        result = number_1 % number_2
        print("{} % {} = ".format(number_1, number_2), end="")
        print(result)

    elif operator == "//":
        result = number_1 // number_2
        print("{} % {} = ".format(number_1, number_2), end="")
        print(result)
    
    else:
        print("You have not typed a valid operator, please run the program again.")