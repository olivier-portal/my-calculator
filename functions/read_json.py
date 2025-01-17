import json


def read_json(file):
    """
    Function used to read json file.
    :param file: File path of json file.
    :return: ∅
    """
    with open(file, 'r') as input_file:
        data = json.load(input_file)

    key_list = [int(key) for key in data.keys()]
    for key in key_list:
        data[key] = data.pop(str(key))

    return data
