
import json
from easygui import *
app_title = "tracker"
date = "2026-06-15" 

records= {  "2026-06-15" :{

    "study": { 

        "study_time": 4.5, 

        "goal_completion": 3 

    }, 

    "recovery": { 

        "sleep_time": 7.5, 

        "stress_level": 4, 

        "focus_level": 3  

    }, 

    "social": { 

        "social_time": 2.0 

    } }
}
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
def delete_log(records):
    """Delete one saved daily log after the user confirms."""
    if records == {}:
        msgbox("There are no daily logs to delete.", app_title)
        return records
    #Place the date(the key of the dictionary) in order.
    date_choices = sorted(records.keys())
 
    date_to_delete = choicebox(
        "Choose a date to delete:",
        app_title,
        date_choices
    )
 
    if date_to_delete is None:
        return records
 
    entry_text = format_text(
        date_to_delete,
        records[date_to_delete]
    )
    #Do confirmation before actually deletes the log user chose
    confirm = buttonbox(
        f"Are you sure you want to delete this log?\n\n{entry_text}",
        app_title,
        choices=["Yes", "No"]
    )
 
    if confirm == "Yes":
        del records[date_to_delete]
        msgbox("The daily log has been deleted.", app_title)
    
    if confirm == "NO":
        msgbox("Your logs haven't been deleted",app_title)
 
    return records
delete_log(records)
msgbox(records)





