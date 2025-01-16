import json


def write_json(history, file_path):
    """
    Function used to write in the json file.
    :param history: A list of tuple each corresponding to an operation.
    :param file_path: File path of json file.
    :return: ∅
    """
    list_of_dicts = [{'operation_tuple': item} for item in history]

    with open(file_path, 'w') as output_file:
        json_line = json.dumps(list_of_dicts, indent=4)
        output_file.write(json_line + "\n")
