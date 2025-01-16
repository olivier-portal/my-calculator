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
# from functions.clear_history import clear_history
# from functions.save_history import save_history

def print_main_options():
    """
    Show (print) the options of main() 
    :return: ∅
    """
    print("\nChoose your option:\n1: Start a new calculation\n"
          "2: Start a new calculation using the previous result\n3: Save the history\n4: Clear the history\n5: Show the history\n6: Exit program\n")
    

def main(history):
    """
    Main function used to provide options to the user to exit, enter a new operation with or without the previous result.
    :return: ∅
    """
    user_choice = input("Enter your choice ('h' for help): ")

    match user_choice:
        case "1":
            history.append(calculate())
            main(history)

        case "2":
            if history != []:
                result = history[-1][3]
                print(f"result: {result}\n")
                print(history)
                if history[-1][3] != "None":
                    history.append(calculate(result))
                    print(history)
            else:
                print("No stored results")
                history.append(calculate())
            main(history)

        case "3":
            # save_history(history)
            print("History saved. Current history:\n")
            display_history(history)
            main(history)

        case "4":
            # clear_history(history)
            print("History cleared. Current history:\n")
            display_history(history)
            main(history)

        case "5":
            print("Current history:\n")
            display_history(history)
            main(history)
        
        case "6":
           print("Goodbye.\n")
           exit()

        case "h":
            print_main_options()
            main(history)

        case _:
            print("Wrong input!\nToo BAD!!")
            main(history)

    
    
if __name__ == "__main__":  # The program will be run only if executed directly, not if it is called by another program.

        operation_history = []
        print_main_options()
        main(operation_history)