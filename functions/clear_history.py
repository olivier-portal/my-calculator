import json

def clear_history():
    with open("./json_history.json", "w") as file:
    # Use the `truncate()` method to clear the file's content
        file.truncate()
        file = json.dumps([])
        