"""
Authors : Lorenzo OTTAVIANI, Olivier PORTAL et Thibault CARON.
Date : 15/01/2025 17h04
Aim of the program :
    Execute a calculator.
Inputs : Numbers used in the calculator operations.
Output : Details of the operations executed.
"""

from functions.again import again
from functions.calculate import calculate


def main():
    """
    Main function of the calculator.
    :return: Details of the operations executed.
    """
    operation_history = [calculate()]
    again(operation_history)
    
    
if __name__ == "__main__":  # The program will be run only if executed directly, not if it is called by another program.

    main()
