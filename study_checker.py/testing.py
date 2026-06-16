
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
    #prevent the dictionary is empty if the user uses for the first time 
    if records == {}:
        msgbox("No records have been saved so far")
        return
    all_logs = ""
    for date in sorted(records):
        entry = records[date]
        all_logs += format_text(date,entry)
        all_logs += "-"*30 + "\n\n"
    textbox("There are all your records saved",app_title,all_logs)
view_all_logs(records)





