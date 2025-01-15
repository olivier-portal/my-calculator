import json

def write_json(history, FILE_PATH):
      with open(FILE_PATH, 'w') as output_file:
              json_line = json.dumps(history, sort_keys=True, indent=2), output_file
              output_file.write(json_line + "\n")