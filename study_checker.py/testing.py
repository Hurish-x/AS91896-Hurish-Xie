
import json
from easygui import *
app_title = "tracker"
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
            if  number > max or number < min :
                msgbox(f"Your enter should between {min} and {max}")
                continue
        except ValueError:
            msgbox("Please enter a integer number,such as 3,4,5")
            continue
        return number
    
get_valid_int("67",1,5)







