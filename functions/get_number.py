
def get_number():
    """
    Function use to input a number.
    :return: The number.
    """

    test = False

    while not test:  # Loop that re-asks an input until it is not a number (integer or float).
        number = input("Enter your number: ")
        try:
            number = int(number)
            test = True
        except ValueError:
            try:
                number = float(number)
                test = True
            except ValueError:
                print("\nNot a number!")

    return number
