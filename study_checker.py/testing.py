
import json
from easygui import *
app_title = "tracker"
date = "2026-06-15" 

records = {
    "2026-06-15": {
        "study": {"study_time": 4.5, "goal_completion": 3},
        "recovery": {"sleep_time": 7.5, "stress_level": 4, "focus_level": 3},
        "social": {"social_time": 2.0}
    },
    "2026-06-16": {
        "study": {"study_time": 6.0, "goal_completion": 5},
        "recovery": {"sleep_time": 8.0, "stress_level": 2, "focus_level": 5},
        "social": {"social_time": 1.0}
    },
    "2026-06-17": {
        "study": {"study_time": 3.0, "goal_completion": 2},
        "recovery": {"sleep_time": 6.5, "stress_level": 5, "focus_level": 2},
        "social": {"social_time": 3.5}
    },
    "2026-06-18": {
        "study": {"study_time": 5.0, "goal_completion": 4},
        "recovery": {"sleep_time": 7.0, "stress_level": 3, "focus_level": 4},
        "social": {"social_time": 1.5}
    },
    "2026-06-19": {
        "study": {"study_time": 5.5, "goal_completion": 4},
        "recovery": {"sleep_time": 7.5, "stress_level": 2, "focus_level": 4},
        "social": {"social_time": 2.0}
    },
    "2026-06-20": {
        "study": {"study_time": 2.0, "goal_completion": 1},
        "recovery": {"sleep_time": 8.5, "stress_level": 1, "focus_level": 2},
        "social": {"social_time": 6.0}
    },
    "2026-06-21": {
        "study": {"study_time": 4.0, "goal_completion": 3},
        "recovery": {"sleep_time": 8.0, "stress_level": 2, "focus_level": 3},
        "social": {"social_time": 2.5}
    }
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


def get_average(records, key):
    """Calculate the average value for one category."""

    total = 0

    for date in records:
        total += records[date][key]

    average = total / len(records)
    return average


def analyse_records(records):
    """Analyse all study records and show a summary."""

    if records == {}:
        msgbox("There are no records to analyse.", app_title)
        return

    average_study = get_average(records, "study_time")
    average_social = get_average(records, "social_time")
    average_sleep = get_average(records, "sleep_time")
    average_stress = get_average(records, "stress_level")
    average_goal = get_average(records, "goal_completion")

    highest_study_date = None
    highest_study_time = -1

    for date in records:
        study_time = records[date]["study_time"]

        if study_time > highest_study_time:
            highest_study_time = study_time
            highest_study_date = date

    analysis_text = "Study Record Analysis\n\n"

    analysis_text += f"Total days recorded: {len(records)}\n"
    analysis_text += f"Average study time: {average_study:.1f} hours\n"
    analysis_text += f"Average social time: {average_social:.1f} hours\n"
    analysis_text += f"Average sleep time: {average_sleep:.1f} hours\n"
    analysis_text += f"Average stress level: {average_stress:.1f} / 5\n"
    analysis_text += f"Average goal completion: {average_goal:.1f}%\n\n"

    analysis_text += f"The highest study time was {highest_study_time} hours \
    on {highest_study_date}.\n\n"

    analysis_text += "Conclusion:\n"

    if average_sleep < 7:
        analysis_text += "- The average sleep time is low, which may affect \
        focus and study performance.\n"
    else:
        analysis_text += "- The average sleep time is healthy, which may \
            support better focus.\n"

    if average_stress >= 4:
        analysis_text += "- The average stress level is high, so the workload\
              may be too heavy.\n"
    elif average_stress >= 2.5:
        analysis_text += "- The average stress level is moderate, so the \
            workload seems manageable.\n"
    else:
        analysis_text += "- The average stress level is low, which suggests \
            the workload is not too stressful.\n"

    if average_goal >= 80:
        analysis_text += "- The goal completion rate is strong, showing that \
            the study routine is effective.\n"
    elif average_goal >= 50:
        analysis_text += "- The goal completion rate is moderate, so the \
            routine works sometimes but could be improved.\n"
    else:
        analysis_text += "- The goal completion rate is low, so the study plan\
              may need to be adjusted.\n"

    textbox(analysis_text, app_title)
analyse_records(records)




