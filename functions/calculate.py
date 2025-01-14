from .get_number import get_number
from .get_operator import get_operator


def calculate():
    """
    Execute a calculator.
    :return: Details of the operations executed.
    """
    number_1 = get_number()
    operator = get_operator()
    number_2 = get_number()

    act = True

    if operator == "/" or operator == "//":
        if number_2 == 0:
            print("Divide by zero is not allowed!")
            act = False
    elif operator == "**":
        if isinstance(number_2, float):
            print("Exponent must be an integer in power calculation.")
            act = False

    if act is True:
        operation = {"+": number_1 + number_2, "-": number_1 - number_2, "*": number_1 * number_2,
                     "/": number_1 / number_2,
                     "//": number_1 // number_2, "%": number_1 % number_2, "**": number_1 ** number_2}

        for k in operation.keys():
            if k == operator:
                result = operation[k]
                if result == int(result):
                    result = int(result)
                print(f"{number_1} {k} {number_2} = ", end="")
                print(result)
