"""
Study Load and Recovery tracker is a program that allows students to 
record their daily study time,social time,sleep time,stress level,focus
level and goal completion.This program aims to help student understand 
what helps them study well by analysing the data
"""
import json
from datetime import datetime
from easygui import *

record_file="record.json"
graph_file="graph.png"
app_title="study Load & Recovery Tracker"
main_menu_options = [
    "Add Daily Log",
    "View All Logs",
    "Search Log by Date",
    "Edit Log",
    "Delete Log",
    "View Data Summary",
    "Generate Graph",
    "View Analysis Conclusion",
    "Save and Exit"
]
def load_record():
    """Load menu from record.json

    Returns:
        list: The loaded list of menu, or an empty list if the file is
        missing or corrupted.
    """
    try:
        with open("./record.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        with open("./record.json", "w") as file:
            json.dump({}, file, indent=2)
            return{}
    except json.JSONDecodeError:
        print("Warning: data file was corrupted. Starting fresh.")
        return {}



def save_record(data):
    """save records to record.json

    catch saving errors print out the reasons
    """
    try:
        with open("record.json", "w") as file:
            json.dump(data, file, indent=2)
    except Exception as e:
        msgbox(f"unable to save:{e}")

    


def get_valid_float(question,min,max):
    """ask user question ,get input value and judge if the inputs are in 
    reasonable range

    Args:question are string parameter used in guibox 
    min and max are float parameter used in "if" judge part

    Return:
    """


    


def get_valid_int():
    pass


def get_valid_date():
    pass


def show_menu():
    pass


def add_daily_log():
    pass


def view_all_logs():
    pass


def search_log():
    pass


def edit_log():
    pass


def delete_log():
    pass


def view_data_summary():
    pass


def generate_graph():
    pass


def analysis():
    pass


def save_exit():
    pass


def main(): 
    pass


if __name__ == "__main__":
    main()