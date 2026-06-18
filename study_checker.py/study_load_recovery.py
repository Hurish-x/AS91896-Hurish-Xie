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


def save_record(records):
    """Save records to record.json

     Arg:Records is the dictionary parameter getting in the load_data 
    function
    """
    try:
        with open("record.json", "w") as file:
            json.dump(records, file, indent=2)
    except Exception as e:
        msgbox(f"unable to save:{e}")

    
def get_valid_float(question,min,max):
    """Ask user question ,get input value and judge if the inputs are in 
    reasonable range

    Args:Question are string parameter used in guibox 
    min and max are float parameter used in "if" judge part

    Return:The function will return the float number for given question
    """
    while True:
        user_input = enterbox(question,app_title)
        if user_input is None:
            return None
        # Get rid of space between input 
        user_input = user_input.strip()
        if user_input == "" :
            msgbox("The value can not be empty")
            continue
        try:
            number = float(user_input)
            if number > max or number < min :
                msgbox(f"Your enter should between {min} and {max}")
                continue
        # In case that user input other kind of string like"abc"
        except ValueError:
            msgbox("Please enter a number,such as 2.5,6")
            continue
        return number


def get_valid_int(question,min,max):
    """Ask user question ,get integer value and judge if the inputs are
    in reasonable range

    Args:Question are string parameter used in guibox 
    min and max are integer number parameter used in "if" judge part

    Return:The function will return the integer number for given 
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
            # Check if the input is in range
            if number > max or number < min :
                msgbox(f"Your enter should between {min} and {max}")
                continue
        except ValueError:
            msgbox("Please enter a integer number,such as 3,4,5")
            continue
        return number


def show_menu():
    pass


def add_daily_log(records):
    """ Getting data from user and add new record to the previous
    dictionary

    Arg:Records is the dictionary parameter getting in the load_data 
    function
    """
    time = datetime.now().strftime("%d-%m-%Y")
    study_time = get_valid_float("How much time do you study today", 0,24)

    # Prevent code breaks if user does not enter in get_valid_float 
    #Function,and send previous dictionary to records
    if study_time is None:
        return records
    social_time = get_valid_float(
        "How much time do you connect with friends or famiy?", 0, 24)
    if social_time is None:
        return records
    sleep_time = get_valid_float(
        "How much time do you sleep last night?", 0,24)
    if sleep_time is None:
        return records
    stress_level = get_valid_int(
        "How stressful do you think you are today?(You need to enter a integer \
        number from 1-5 and 1 is lowerst)",1,5)
    if stress_level is None:
        return records
    focus_level = get_valid_int(
        "How concentrated do you think you are today?(you need to enter a  \
        integer number from 1-5 and 1 is lowest)",
        1,
        5
    )
    if focus_level is None:
        return records
    goal_completion = get_valid_int(
        "How concentrated do you think you are today?(you need to enter\
        a integer number from 1-5 and 1 is lowest)",
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
            "stress_level":stress_level,
            "focus_level":focus_level
        },
        "social":{
            "social_time":social_time
        }
    }
    records[time] = daily_entry
    msgbox(app_title,"The log have been saved successfully")


def format_text(date,entry):
    """format the dictionary into readable text
    
    Args:date is the key value in the nested dictionary
    """
    log_text = (
        f"Date:{date}\n"
        f"Study time:{entry["study"]["study_time"]} hours\n"
        f"Goal Completion:{entry["study"]["goal_completion"]}/5\n"
        f"Sleep Time:{entry["recovery"]["sleep_time"]} hours\n"
        f"Stress Level:{entry["recovery"]["stress_level"]}/5\n"
        f"Focus Level:{entry["recovery"]["focus_level"]}/5\n"
        f"Social Time:{entry["social"]["social_time"]} hours\n"
    )
    return log_text


def view_all_logs(records):
    """show all saved logs to users in readable form

    Args: record is the dictionary parameter getting in the load_data 
    function 
    """
    #prevent the dictionary is empty if the user uses for the first time 
    if records == {}:
        msgbox("No records have been saved so far")
        return
    all_logs = ""
    #add formatted text in empty string and put in  textbox to display
    for date in sorted(records):
        entry = records[date]
        all_logs += format_text(date,entry)
        all_logs += "-"*30 + "\n\n"
    textbox("There are all your records saved",app_title,all_logs)


def search_log():
    pass


def edit_log(records):
    """Edit one field in an existing daily log.

    Return:Return new records to json document
    """
    if records == {}:
        msgbox("There are no daily logs to edit.", app_title)
        return records

    date_choices = sorted(records.keys())

    date_to_edit = choicebox(
        "Choose a date to edit:",
        app_title,
        date_choices
    )

    if date_to_edit is None:
        return records

    current_log = format_text(date_to_edit, records[date_to_edit])
    field_to_edit = buttonbox(
        f"Current log:\n\n{current_log}\n\nWhat do you want to edit?",
        app_title,
        choices=[
            "Study Time",
            "Sleep Time",
            "Social Time",
            "Stress Level",
            "Focus Level",
            "Goal Completed",
            "Cancel"
        ]
    )
    #Based on what button users choose ,update new data to dictionary.
    if field_to_edit == "Cancel" or field_to_edit is None:
        return records
    if field_to_edit in ["Study Time" , "Goal Completion"]:
        if field_to_edit == "Study Time" :
            new_value = get_valid_float(f"Enter the new {field_to_edit}:", 0, 
                                        24)
        if field_to_edit == "Goal Completion" :
            new_value = get_valid_int(f"Enter the new {field_to_edit}:", 1, 
                                        5)
        if new_value is None:
             return records
        #Correct the format in our key value form.
        entry = "_".join(field_to_edit.lower().split())
        records[date_to_edit]["study"][entry] = new_value

    if field_to_edit in ["Sleep Time", "Stress Level", "Focus Level"]:
        if field_to_edit == "Sleep Time" :
            new_value = get_valid_float(f"Enter the new {field_to_edit}:", 0, 
                                        24)
        if field_to_edit == "Stress Level" or "Focus Level" :
            new_value = get_valid_int(f"Enter the new {field_to_edit}:", 1, 
                                        5)
        if new_value is None:
             return records
        entry = "_".join(field_to_edit.lower().split())
        records[date_to_edit]["recovery"][entry] = new_value

    if field_to_edit == "Social Time":
        new_value = get_valid_float(f"Enter the new {field_to_edit}:", 0, 
                                        24)
        if new_value is None:
            return records
        entry = "_".join(field_to_edit.lower().split())
        records[date_to_edit]["social"][entry] = new_value

    msgbox("The daily log has been updated.", app_title)
    return records

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