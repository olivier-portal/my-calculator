import json

def write_json(history, FILE_PATH):
      with open(FILE_PATH, 'w') as output_file:
            list_of_dicts = [{'operation_tuple': item} for item in history]
            json_line = json.dumps(list_of_dicts)
            output_file.write(json_line + "\n")