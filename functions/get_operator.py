def get_operator():
    """
    Function use to input an operator.
    :return: An operator.
    """
    display_operator = ("\nChoose one of these operators:\n+: addition\n-: subtraction\n* or x: multiplication"
                        "\n/: division\n^ or **: power\n//: floor division\n%: modulo (remainder of division)\n")

    user_operator = input("Enter your operator: ")

    match user_operator:  # Checks if the operator is one of those admitted.
        case "+":
            operator = "+"
        case "-":
            operator = "-"
        case "*":
            operator = "*"
        case "x":
            operator = "*"
        case "/":
            operator = "/"
        case "^":
            operator = "**"
        case "**":
            operator = "**"
        case "//":
            operator = "//"
        case "%":
            operator = "%"
        case _:  # Case of a wrong input.
            print(display_operator)  # Display a help with the list of all corrects operators.
            operator = get_operator()  # Re-asks an input until it is not a correct operator.

    return operator
        