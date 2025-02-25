def display_history(history):
    """
    Function to display the history of operations.
    :param: history: The dictionary of operations history.
    :return: ∅
    """
    if not history:
        print("No operations performed yet.")
    else:
        print("\nOperation History:")
        for index, (number_1, operation, number_2, result) in enumerate(list(history.values()), start=1):
            print(f"{index}. {number_1} {operation} {number_2} = {result}")
