import json


def read_json(file):
    """
    Function used to retrieve from a json file, the past operations history and convert there into a dictionary.
    Executed at the beginning of the program.
    :param file: File path of json file.
    :return: A dictionary of operations history.
    """
    with open(file, 'r') as input_file:  # Deserializing from a json format.
        data = json.load(input_file)

    key_list = [int(key) for key in data.keys()]  # Convert json keys from strings to integers.
    for key in key_list:
        data[key] = data.pop(str(key))

    return data
