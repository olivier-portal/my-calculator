import json

def read_json(FILE_PATH):
      with open(FILE_PATH, 'r') as input_file:
            print(json.load(input_file))
