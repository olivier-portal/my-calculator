def normalize_item(item):
    """
    Function used to correct json structure.
    :param item: A key of a json dictionary.
    :return: The key.
    """
    if isinstance(item, dict) and "operation_tuple" in item:
        return item["operation_tuple"]
    return item
