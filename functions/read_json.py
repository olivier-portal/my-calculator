import json
# from .normalize_item import normalize_item

# item = {"operation_tuple": []}
# normalize_item(item)

def read_json(FILE_PATH):
      with open(FILE_PATH, 'r') as input_file:
            data = json.load(input_file)
            # return [normalize_item(entry) for entry in data]
            return data
      
print(read_json(FILE_PATH="json_history.json"))