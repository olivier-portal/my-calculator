from .calculate import calculate
from .display_history import display_history
from .write_json import write_json

FILE_PATH = "./json_history.json"


def again(history):
    """
    Function used to provide options to the user to exit, enter a new operation with or without the previous result.
    :return: ∅
    """
    print("\nDo you want to calculate again?\nChoose your option:\n1: Start a new calculation\n"
          "2: Start a new calculation using the previous result\n3: Show the history and exit\n")

    user_choice = input("Enter your choice: ")

    match user_choice:
        case "1":
            history.append(calculate())
            write_json(history, FILE_PATH)
            again(history)

        case "2":
            result = history[-1][3]
            print(f"result: {result}\n")
            history.append(calculate(result))
            write_json(history, FILE_PATH)
            again(history)

        case "3":
            write_json(history, FILE_PATH)
            display_history(history)
            print("\nSee you later.")

        case _:
            print("Wrong input!\nToo BAD!!")
            again(history)
