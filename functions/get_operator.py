def get_operator():
    """
    Function use to input an operator.
    :return: An operator.
    """
    display_operator = ("\nChoose one of these operators:\n+: addition\n-: subtraction\n* or x: multiplication"
                        "\n/: division\n^ or **: power\n//: floor division\n%: modulo (remainder of division)\n")

    user_operator = input("Enter your operator: ")

    match user_operator:
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
        case _:
            print(display_operator)
            operator = get_operator()

    return operator
        