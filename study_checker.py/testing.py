
import json
from easygui import *
app_title = "tracker"
def format_text(date,entry):
    """format the dictionary into readable text
    
    Args:date is the key value in the nested dictionary
    """
    log_text = (
        f"Date:{date}\n"
        f"Study time: {entry["study"]["study_time"]} hours\n"
        f"Goal Completion: {entry["study"]["goal_completion"]}\n"
        f"Sleep Time: {entry["recovery"]["sleep_time"]} hours\n"
        f"Stress Level: {entry["recovery"]["stress_level"]}\n"
        f"Focus Level: {entry["recovery"]["focus_level"]}\n"
        f"Social Time: {entry["social"]["social_time"]} hours\n"
    )
    return log_text
print(format_text(date = "2026-06-15",entry = {
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
    }
}))







