import json


def clear_history():
    """
    Function used to clear json history.
    :return: ∅
    """
    with open("./json_history.json", "w") as file:
        file.truncate()   # Use the truncate method to clear the file's content.

        # Rewrote "{}" in the empty file to avoid an error, in which the file was not recognized as a json format.
        json.dump({}, file)
        