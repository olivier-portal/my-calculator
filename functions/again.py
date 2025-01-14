from .calculate import calculate

def again():
    calc_again = input("""
Do you want to calculate again?
Please type Y for YES or N for NO.
""")

    if calc_again.upper() == "Y":
        calculate()
        again()
    elif calc_again.upper() == "N":
        print("See you later.")
    else:
        again()