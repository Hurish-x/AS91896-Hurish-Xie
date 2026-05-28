import json
from datetime import datetime

def load_record():
    """Load menu from record.json

    Args:
        filename (str): The JSON filename to load.

    Returns:
        list: The loaded list of menu, or an empty list if the file is
        missing or corrupted.
    """
    try:
        with open("record.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        with open("record.json", "w") as file:
            json.dump({}, file, indent=2)
    except json.JSONDecodeError:
        print("Warning: data file was corrupted. Starting fresh.")
        return {}
load_record()