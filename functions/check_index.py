def check_index(history):
    """
    Check the index of the last operation in operations history.
    Set the index at 0 if the history is empty.
    :param history: A dictionary of operations history.
    :return: The index of the last operation in operations history.
    """
    if history != {}:  # Check if the history is empty.
        last_index = next(reversed(history.keys()))  # Take the last index of operations history.
    else:
        last_index = 0
    return last_index