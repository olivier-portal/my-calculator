def get_number():
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
