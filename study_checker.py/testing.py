
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
def edit(records):
    field_to_edit = enterbox()
    if field_to_edit in ["Study Time" , "Goal Completion"]:
        if field_to_edit == "Study Time":
            new_value = get_valid_float(f"Enter the new {field_to_edit}:", 0, 
                                        24)
        if field_to_edit == "Goal Completion" :
            new_value = get_valid_int(f"Enter the new {field_to_edit}:", 1, 
                                        5)
        if new_value is None:
             return records
        #Correct the format in our key value form.
        entry = "_".join(field_to_edit.lower().split())
        records["2026-06-15"]["study"][entry] = new_value
        return records
        

print(edit(records))






