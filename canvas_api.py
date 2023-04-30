import bakery_canvas
from nicegui import ui
#import requests
import datetime
#import pymongo

def current_courses(key):
    courses = bakery_canvas.get_courses(key)
    spring23 = datetime.datetime(2023,1,24)
    current = []
    for course in courses:
        if course.end_at:
            course.end_at = course.end_at[0:10]
            year = int(course.end_at[0:4])
            month = int(course.end_at[6:7])
            day = int(course.end_at[9:10])
            as_datetime = datetime.datetime(year,month,day)
            if as_datetime > spring23:
                current.append(course.name)
    return current

def create_dict(key:str):
    split_key = key.splitlines()
    name = split_key[0]
    email = split_key[1]
    key = split_key[2]
    return {name: current_courses(key)}
def create_common_classes(user: dict,database: dict):
    return list(set(user.values).intersection(database.values))
