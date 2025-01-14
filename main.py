"""
Authors : Lorenzo OTTAVIANI, Olivier PORTAL et Thibault CARON.
Date : 14/01/2025 14h39
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
    calculate()
    again()
    
    
if __name__ == "__main__":  # The program will be run only if executed directly, not if it is called by another program.
    main()
