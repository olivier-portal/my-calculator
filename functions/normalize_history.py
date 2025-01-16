def normalize_history(history):
    
    def normalize_item(item):
        if isinstance(item, dict) and "operation_tuple" in item:
            return item["operation_tuple"]
        return item
    
    return [normalize_item(item) for item in history]
    