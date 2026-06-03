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

    Return:the function will return the float number for given question
    """
    while True:
        user_input = enterbox(question,app_title)
        if user_input is None:
            return None
        user_input = user_input.strip()
        if user_input == "" :
            msgbox("The value can not be empty")
            continue
        try:
            number = float(user_input)
        except ValueError:
            msgbox("Please enter a number,such as 2.5,6")
            continue
        return number


def get_valid_int(question,min,max):
    """ask user question ,get integer value and judge if the inputs are
    in reasonable range

    Args:question are string parameter used in guibox 
    min and max are integer number parameter used in "if" judge part

    Return:the function will return the integer number for given 
    question
    """
    while True:
        user_input = enterbox(question,app_title)
        if user_input is None:
            return None
        user_input = user_input.strip()
        if user_input == "" :
            msgbox("The value can not be empty")
            continue
        try:
            number = int(user_input)
        except ValueError:
            msgbox("Please enter a integer number,such as 3,4,5")
            continue
        return number


def show_menu():
    pass


def add_daily_log(records):
    """ Getting data from user and add new record to the previous
    dictionary

    Arg:record is the dictionary parameter getting in the load_data 
    function
    """
    time = datetime.now().strftime("%d-%m-%Y")
    study_time = get_valid_float("How much time do you study today",
                                 0,
                                 24)
    if study_time is None:
        return records
    social_time = get_valid_float(
        "How much time do you connect with friends or famiy?"
        0,
        24)
    if social_time is None:
        return records
    sleep_time = get_valid_float(
        "How much time do you sleep last night?",
        0,
        24
    )
    if sleep_time is None:
        return records
    stress_level = get_valid_int(
        "How stressful do you think you are today?(you need to enter a\
        integer number from 1-5 and 1 is lowerst)",
        1,
        5
    )
    if stress_level is None:
        return records
    focus_level = get_valid_int(
        "How concentrated do you think you are today?(you need to enter\
        a integer number from 1-5 and 1 is lowest)"
        1,
        5
    )
    if focus_level is None:
        return records
    goal_completion = get_valid_int(
        "How concentrated do you think you are today?(you need to enter\
        a integer number from 1-5 and 1 is lowest)"
        1,
        5
    )
    if focus_level is None:
        return records
    
    daily_entry = {
        "study": {
            "study_time":study_time,
            "goal_completion":goal_completion
        },
        "recovery":{
            "sleep_time":sleep_time,
            

        }
    }
    
    
    


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
    records = load_record()
    records = add_daily_log(records)


if __name__ == "__main__":
    main()