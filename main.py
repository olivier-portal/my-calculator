"""
Authors : Lorenzo OTTAVIANI, Olivier PORTAL et Thibault CARON.
Date : 15/01/2025 17h04
Aim of the program :
    Execute a calculator.
Inputs : Numbers used in the calculator operations.
Output : Details of the operations executed.
"""

from functions.calculate import calculate
from functions.display_history import display_history
from functions.clear_history import clear_history
from functions.read_json import read_json
from functions.write_json import write_json
from functions.print_main_options import print_main_options

FILE_PATH = "./json_history.json"


def main(history):
    """
    Main function used to provide options to the user to exit, enter a new operation with or without the previous result.
    :return: ∅
    """
    user_choice = input("\nEnter your choice ('h' for help): ")

    match user_choice:
        case "1":
            history.append(calculate())
            write_json(history, FILE_PATH)
            main(history)

        case "2":
            if history != []:
                result = history[-1][3]
                print(f"result: {result}\n")
                if history[-1][3] != "None":
                    history.append(calculate(result))
                    write_json(history, FILE_PATH)
            else:
                print("No stored results")
                history.append(calculate())
                write_json(history, FILE_PATH)
            main(history)

        case "3":
            write_json(history, FILE_PATH)
            display_history(history)
            main(history)

        case "4":
            history = []
            clear_history()
            print("History cleared. Current history:\n")
            display_history(history)
            main(history)
        
        case "5":
           print("Goodbye.\n")
           exit()

        case "h":
            print_main_options()
            main(history)

        case _:
            print("Wrong input!\nToo BAD!!")
            main(history)


if __name__ == "__main__":  # The program will be run only if executed directly, not if it is called by another program.

    operation_history = read_json(FILE_PATH)

    print_main_options()
    main(operation_history)