import json

def normalize_item(item):
    if isinstance(item, dict) and "operation_tuple" in item:
        return item["operation_tuple"]
    return item

def read_json(FILE_PATH):
      with open(FILE_PATH, 'r') as input_file:
            data = json.load(input_file)
            return [normalize_item(entry) for entry in data]