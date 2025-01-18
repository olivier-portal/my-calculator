import json


def write_json(history, file):
    """
    Function used to write the operations history in the json file.
    :param history: The dictionary of operations history.
    :param file: File path of json file.
    :return: ∅
    """
    json_object = json.dumps(history, indent=4)  # Serializing in a json format.

    with open("./json_history.json", "w") as file:  # Write th in json_history.json
        file.write(json_object)
