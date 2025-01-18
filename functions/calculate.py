from .get_number import get_number
from .get_operator import get_operator


def calculate(result="None"):
    """
    Function used to perform the calculation based on the inputs.
    By default, the previous result is ignored.
    :param: result: The previous result in the history.
    :return: A list that contains the two terms of the operation, the operator and the result.
    """
    print()  # Skip a line before the operation.

    # Uses the last result as the first term of the operation, otherwise asks the user to enter another one.
    if result == "None":
        number_1 = get_number()  # Call the function used to choose a number.
    else:
        number_1 = result

    operator = get_operator()  # Call the function used to choose an operator.

    correct = False  # Used to check if operation is correct.

    # Loop used to ask the user to re-enter the second term of the operation until the operation is correct.
    while correct is False:
        number_2 = get_number()
        print()  # Skip a line after the operation.
        correct = True

        if operator == "**":  # Used to restrict operations with an exponential to integer powers.
            if isinstance(number_2, float):
                print("Exponent must be an integer in power calculation.")
                correct = False

        if correct is True:
            try:
                operation = {"+": number_1 + number_2, "-": number_1 - number_2, "*": number_1 * number_2,
                             "/": number_1 / number_2, "//": number_1 // number_2, "%": number_1 % number_2,
                             "**": number_1 ** number_2}

                for k in operation.keys():  # Read the operation dictionary and execute the operation.
                    if k == operator:
                        result = operation[k]
                        if result == int(result):  # Transform result into an integer when it is already one.
                            result = int(result)
                        print(f"{number_1} {k} {number_2} = ", end="")
                        print(result)

            except ZeroDivisionError:
                print("Divide by zero is not allowed!")
                correct = False

    return [number_1, operator, number_2, result]
