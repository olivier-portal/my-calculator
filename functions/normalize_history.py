from .normalize_item import normalize_item

def normalize_history(history):
    item = {"operation_tuple": []}
    normalize_item(item)
    
    return [normalize_item(item) for item in history]
    