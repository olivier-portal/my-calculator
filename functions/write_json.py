import json

def write_json(history, FILE_PATH):
      # Serializing json
      json_object = json.dumps(history, indent=4)
      # print(json_object)
 
      # Writing to json_history.json
      with open("./json_history.json", "w") as FILE_PATH:
            FILE_PATH.write(json_object) 