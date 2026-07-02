"""
Study Load and Recovery tracker is a program that allows students to 
record their daily study time,social time,sleep time,stress level,focus
level and goal completion.This program aims to help student understand 
what helps them study well by analysing the data
"""
import json
from datetime import datetime
from easygui import *
import matplotlib.pyplot as plt
import os
import matplotlib.patches as mpatches

record_file="record.json"
graph_file="graph.png"
app_title="study Load & Recovery Tracker"
main_menu_options = [
    "Add Daily Log",
    "View All Logs",
    "Edit Log",
    "Delete Log",
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
        msgbox("Warning: data file was corrupted. Starting fresh.")
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


def add_daily_log(records):
    """ Getting data from user and add new record to the previous
    dictionary

    Arg:Records is the dictionary parameter getting in the load_data 
    function
    """
    time = datetime.now().strftime("%d-%m-%Y")
    study_time = get_valid_float("How much time did you study today", 0,24)

    # Prevent code breaks if user does not enter in get_valid_float 
    #Function,and send previous dictionary to records
    if study_time is None:
        return records
    social_time = get_valid_float(
        "How much time did you connect with friends or famiy?", 0, 24)
    if social_time is None:
        return records
    sleep_time = get_valid_float(
        "How much time did you sleep last night?", 0,24)
    if sleep_time is None:
        return records
    stress_level = get_valid_int(
        "How stressful were you today?(You need to enter a  \
        integer number from 1-5 and 1 is lowerst)",1,5)
    if stress_level is None:
        return records
    focus_level = get_valid_int(
        "How concentrated were you today?(you need to enter a  \
        integer number from 1-5 and 1 is lowest)",
        1,
        5
    )
    if focus_level is None:
        return records
    goal_completion = get_valid_int(
        "How did you finish your work today?(you need to enter\
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
    msgbox("The log have been saved successfully",app_title)
    return records

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


def edit_log(records):
    """Edit one field in an existing daily log.

    Return:Return new records to json document.
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
 

def delete_log(records):
    """Delete one saved daily log after the user confirms.
    
    Return:Return new records to json document.
    """
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


def get_average(records,field,key):
    """Calculate the average value for one category.
    
    Args:"field" is the key in the inner dictinary after date."key"is the key 
    in the smallest dictionary
    """

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

    average_study = get_average(records,"study" "study_time")
    average_social = get_average(records,"social" "social_time")
    average_sleep = get_average(records, "recovery","sleep_time")
    average_stress = get_average(records,"recovery", "stress_level")
    average_goal = get_average(records, "study"",goal_completion")
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
            benefit your mental health"
    elif average_social <= 0.5 :
        analysis_text += "The social time is low,so you may need to connect\
            more with your friends or family\n"

    msgbox(analysis_text, app_title)


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
    red_patch = mpatches.Patch(color='red', label="Focus Level")
    
    ax1.set_xlabel("Date")
    ax1.set_ylabel("Sleep Time (Hours)")
 
    ax2 = ax1.twinx()
    ax2.plot(dates, focus_levels,c="red", marker="o", label="Focus Level")
    blue_patch = mpatches.Patch(color='blue', label="Sleep Time")
    plt.legend(handles=[red_patch, blue_patch], loc='upper right', framealpha
               =0.8)
    ax2.set_ylabel("Focus Level (1-5)")
 
    plt.title("Sleep Time and Focus Level Over Time")
    plt.xticks(rotation=45)
    fig.tight_layout()
    plt.grid(True)
    file_path = os.path.join("./analysis_image","sleep_focus_graph.png")
    plt.savefig(file_path)
    plt.close()
 
    # Graph 2: Stress level and goal completion over time
    fig, ax2 = plt.subplots(figsize=(10, 5))
 
    ax2.plot(dates, goal_completion, c="cyan",marker="o", label="Goal " \
    "Completion")
    cyan_patch = mpatches.Patch(color="cyan", label="Goal Completion")
    ax2.set_xlabel("Date")
    ax2.set_ylabel("Goal Completion(1-5)")
 
    ax3 = ax2.twinx()
    ax3.plot(dates, stress_levels,c="brown", marker="o", label="Stress Level")
    brown_patch = mpatches.Patch(color="brown", label="Stress Level")
    plt.legend(handles=[cyan_patch, brown_patch], loc='upper right', framealpha
               =0.8)
    ax3.set_ylabel("Stress Level (1-5)")
 
    plt.title("Goal Completion and Stress Level")
    plt.xticks(rotation=45)
    fig.tight_layout()
    plt.grid(True)
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
    

def main(): 
    records = load_record()
    while True:
        choice = buttonbox("What would you like to do?",app_title,
                           choices=main_menu_options)
        if choice == "Add Daily Log":
            records = add_daily_log(records)
            save_record(records)

        elif choice == "View Logs":
            view_all_logs(records)

        elif choice == "Edit Log":
            records = edit_log(records)
            save_record(records)

        elif choice == "Delete Log":
            records = delete_log(records)
            save_record(records)

        elif choice == "Analyse Data":
            analyse_records(records)

        elif choice == "Generate Graph":
            generate_graph(records)

        elif choice == "Save and Exit" or choice is None:
            save_record(records)
            msgbox("Thanks for using this program!", app_title)
            break
if __name__ == "__main__":
    main()