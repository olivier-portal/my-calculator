from .calculate import calculate
from .display_history import display_history


def again(history):
    """
    Function used to provide options to the user to exit, enter a new operation with or without the previous result.
    :return: ∅
    """
    calc_again = input("""
Do you want to calculate again?
Please type Y for YES or N for NO,
P to start a new calculation using the previous result
""")

    if calc_again.upper() == "Y":
        history.append(calculate())
        again(history)

    elif calc_again.upper() == "P":
        result = history[-1]
        result = result[3]
        print(f"result: {result}")
        history.append(calculate(result))
        again(history)

    elif calc_again.upper() == "N":
        display_history(history)
        print("See you later.")

    else:
        print("Too BAD!!")
        again(history)
