
import json
from easygui import *
def save_record(data):
    """save records to record.json

    catch saving errors print out the reasons
    """
    try:
        with open("record.json", "w") as file:
            json.dump(data, file, indent=2)
    except Exception as e:
        msgbox(f"unable to save:{e}")







