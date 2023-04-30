import bakery_canvas
from nicegui import ui
import requests
import datetime
import pymongo

def print_courses(courses):
    for course in courses:
        return course.name
def current_courses(courses):
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
                current.append(course)
    return current