import json


def clear_history():
    """
    Function used to clear json history.
    :return: ∅
    """
    with open("./json_history.json", "w") as file:
        file.truncate()   # Use the `truncate()  method to clear the file's content
        json.dump({}, file)
        