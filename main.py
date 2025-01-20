"""
Authors : Lorenzo OTTAVIANI, Olivier PORTAL et Thibault CARON.
Date : 18/01/2025 15h41
Aim of the program :
    Execute a calculator.
Inputs : Numbers and operators used in the calculator operations.
Output : Details of the operations executed.
"""

from functions.calculate import calculate
from functions.check_index import check_index
from functions.clear_history import clear_history
from functions.display_history import display_history
from functions.display_menu import display_menu
from functions.read_json import read_json
from functions.write_json import write_json


FILE_PATH = "./json_history.json"


def main(history, index):
    """
    Main function used to provide options to the user to exit or enter a new operation,
    with or without the previous result.
    :param: history: A dictionary of operations history.
    :param: index: The index of the last operation in operations history.
    :return: ∅
    """
    user_choice = input("\nEnter your choice ('h' for help): ")  # Ask the user to choose one of the menu options.

    match user_choice:
        case "1":  # Perform a new operation.
            index += 1
            history[index] = calculate()  # Add the last operation to the dictionary of operations history.
            write_json(history, FILE_PATH)  # Update history saved in the json file.
            main(history, index)  # Rerun the choice of menu options again.

        case "2": # Perform an operation using the last result as first term
            if history != {}:  # Check if operations history is empty.
                result = history[index][3]
                print(f"\nLast result: {result}")  # Print the last result.
                if history[index][3] != "None":
                    index += 1
                    history[index] = calculate(result)
                    write_json(history, FILE_PATH)
            else:  # Case of an empty history, perform a new operation, like in case 1.
                print("\nNo stored results!")
                index += 1
                history[index] = calculate()
                write_json(history, FILE_PATH)
            main(history, index)

        case "3":  # Clear the history.
            history = {}
            clear_history()
            print("History cleared! Current history:\n")
            display_history(history)
            main(history, index)

        case "4":  # Display the history.
            write_json(history, FILE_PATH)
            display_history(history)
            main(history, index)

        case "5":  # Exit the program.
            print("Goodbye.\n")
            exit()

        case "h":  # Display menu again.
            display_menu()
            main(history, index)

        case _:  # Case of a wrong input.
            print("Wrong input!\nToo BAD!!")
            main(history, index)


if __name__ == "__main__":  # The program will be run only if executed directly, not if it is called by another program.

    # Store in a dictionary the operations history retrieved from the json file.
    operations_history = read_json(FILE_PATH)

    display_menu()
    main(operations_history, check_index(operations_history))
