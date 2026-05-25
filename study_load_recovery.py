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
app_title="study Load&Rcovery Tracker"
subject=[accounting, agriculture, biology, business, chemistry, chinese,
 classical, dance, design, digital, drama, earth, economics, english,
french, geography, german, health, history, japanese, latin,
 mathematics, media, music, physical, physics, psychology, religious,
  science, spanish, statistics, visuals]