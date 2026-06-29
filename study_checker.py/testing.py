
import json
from easygui import *
import os
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


def get_average(records,field,key):
    """Calculate the average value for one category."""

    total = 0

    for date in records:
        total += records[date][field][key]

    average = total / len(records)
    return average

def analyse_records(records):
    """Analyse all study records and show a summary."""

    if records == {}:
        msgbox("There are no records to analyse.", app_title)
        return

    average_study = get_average(records,"study", "study_time")
    average_social = get_average(records,"social" ,"social_time")
    average_sleep = get_average(records, "recovery","sleep_time")
    average_stress = get_average(records,"recovery", "stress_level")
    average_goal = get_average(records, "study","goal_completion")
    average_focus = get_average(records,"recovery","focus_level")
    highest_study_date = None
    highest_study_time = -1

    for date in records:
        study_time = records[date]["study"]["study_time"]

        if study_time > highest_study_time:
            highest_study_time = study_time
            highest_study_date = date

    analysis_text = "Study Record Analysis\n\n"

    analysis_text += f"Total days recorded: {len(records)}\n"
    analysis_text += f"Average study time: {average_study:.1f} hours\n"
    analysis_text += f"Average stress level: {average_focus:.1f} / 5\n"
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

    if average_goal >= 8:
        analysis_text += "- The goal completion rate is strong, showing that \
            the study routine is effective.\n"
    elif average_goal >= 5:
        analysis_text += "- The goal completion rate is moderate, so the \
            routine works sometimes but could be improved.\n"
    else:
        analysis_text += "- The goal completion rate is low, so the study plan\
              may need to be adjusted.\n"
    
    if average_social >= 1:
        analysis_text += "The social time you have is exemplary,which may \
            benefit your mental health."
    elif average_social <= 0.5 :
        analysis_text += "The social time is low,so you may need to connect\
            more with your friends or family.\n"
    textbox(analysis_text, app_title)


import matplotlib.pyplot as plt
 
def generate_graph(records):
    """Generate  line graphs to show the tendency of each two variables
    and bar graph to show the whole performance of users.
    """
    if len(records) == 0:
        msgbox("No records found.", app_title)
        return
 
    dates = sorted(records.keys())
 
    sleep_times = []
    focus_levels = []
    stress_levels = []
    goal_completion = []
    study_times = []
    social_times = []
 
    for date in dates:
        entry = records[date]
 
        study_times.append(entry["study"]["study_time"])
        goal_completion.append(entry["study"]["goal_completion"])
 
        sleep_times.append(entry["recovery"]["sleep_time"])
        stress_levels.append(entry["recovery"]["stress_level"])
        focus_levels.append(entry["recovery"]["focus_level"])
 
        social_times.append(entry["social"]["social_time"])
 
    # Graph 1: Sleep time and focus level over time
    fig, ax1 = plt.subplots(figsize=(10, 5))
 
    ax1.plot(dates, sleep_times, c="blue",marker="o", label="Sleep Time")
    ax1.set_xlabel("Date")
    ax1.set_ylabel("Sleep Time (Hours)")
 
    ax2 = ax1.twinx()
    ax2.plot(dates, focus_levels,c="red", marker="o", label="Focus Level")
    ax2.set_ylabel("Focus Level (1-5)")
 
    plt.title("Sleep Time and Focus Level Over Time")
    plt.xticks(rotation=45)
    fig.tight_layout()
    file_path = os.path.join("./analysis_image","sleep_focus_graph.png")
    plt.savefig(file_path)
    plt.close()
 
    # Graph 2: Stress level and goal completion over time
    fig, ax2 = plt.subplots(figsize=(10, 5))
 
    ax2.plot(dates, goal_completion, c="blue",marker="o", label="Goal Completion")
    ax2.set_xlabel("Date")
    ax2.set_ylabel("Sleep Time (Hours)")
 
    ax3 = ax2.twinx()
    ax3.plot(dates, stress_levels,c="red", marker="o", label="Stress Level")
    ax3.set_ylabel("Stress Level (1-5)")
 
    plt.title("Goal Completion and Stress Level")
    plt.xticks(rotation=45)
    fig.tight_layout()
    file_path = os.path.join("./analysis_image","goal_stress_graph.png")
    plt.savefig(file_path)
    plt.close()


    # Graph 3: Average time bar chart
    average_study = sum(study_times) / len(study_times)
    average_sleep = sum(sleep_times) / len(sleep_times)
    average_social = sum(social_times) / len(social_times)
 
    categories = ["Study Time", "Sleep Time", "Social Time"]
    averages = [average_study, average_sleep, average_social]
 
    plt.figure(figsize=(8, 5))
    plt.bar(categories, averages, width = 0.2)
    plt.title("Average Daily Time")
    plt.xlabel("Category")
    plt.ylabel("Average Hours")
    plt.tight_layout()
    file_path = os.path.join("./analysis_image","average_time_bar_graph.png")
    plt.savefig(file_path)
    plt.close()
 
    msgbox(
        "Graphs generated successfully saved to 'analysis_image' folder:\n\n"
        "1. sleep_focus_graph.png\n"
        "2. stress_goal_graph.png\n"
        "3. average_time_bar_graph.png",
        app_title
    )

generate_graph(records)


