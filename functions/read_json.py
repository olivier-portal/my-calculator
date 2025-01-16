import json
from .normalize_item import normalize_item

item = {"operation_tuple": []}
normalize_item(item)


def read_json(file_path):
    """
    Function used to read json file.
    :param file_path: File path of json file.
    :return: ∅
    """
    with open(file_path, 'r') as input_file:
        data = json.load(input_file)
        return [normalize_item(entry) for entry in data]
