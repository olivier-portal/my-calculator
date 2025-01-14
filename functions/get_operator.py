def get_operator():
    """
    Function use to input an operator.
    :return: An operator.
    """
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
    
    return operator
        