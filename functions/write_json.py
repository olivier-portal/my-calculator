import json


def write_json(history, FILE_PATH):
      list_of_dicts = [{'operation_tuple': item} for item in history]
      
      with open(FILE_PATH, 'w') as output_file:
            json_line = json.dumps(list_of_dicts, indent=4)
            output_file.write(json_line + "\n")