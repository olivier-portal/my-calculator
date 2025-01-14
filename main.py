from functions.again import again
from functions.calculate import calculate

def main():
    calculate()
    again()
    # user_choice = input("Do you want to get the result or add more numbers? \nEnter '=' to get the result \nEnter a to add more numbers")
    # if user_choice == "=":
    #     do_operation()
    # elif user_choice == "a":
    #     get_number()
    # else:
    #     print("You must enter '=' or 'a'")
    
    
if __name__ == "__main__":  # The program will be run only if executed directly, not if it is called by another program.
    main()