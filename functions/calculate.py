from .get_number import get_number
from .get_operator import get_operator


def calculate(result="None"):
    """
    Function used to perform the calculation based on the inputs.
    :result: A result chosen from history.
    :return: A tuples of the inputs and the result of the operation.
    """
    if result == "None":
        number_1 = get_number()
    else:
        number_1 = result

    operator = get_operator()

    number_2 = get_number()
    print()
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

    return number_1, operator, number_2, result
