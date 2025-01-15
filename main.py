"""
Authors : Lorenzo OTTAVIANI, Olivier PORTAL et Thibault CARON.
Date : 15/01/2025 11h37
Aim of the program :
    Execute a calculator.
Inputs : Numbers used in the calculator operations.
Output : Details of the operations executed.
"""

from functions.again import again
from functions.calculate import calculate
from functions.read_json import read_json
from functions.write_json import write_json

FILE_PATH = "./json_history.json"

def main():
    """
    Main function of the calculator.
    :return: Details of the operations executed.
    """
    
    operation_history = read_json(FILE_PATH)
    calculate()
    write_json(operation_history, FILE_PATH)
    again(operation_history)
    
    
if __name__ == "__main__":  # The program will be run only if executed directly, not if it is called by another program.

    main()
