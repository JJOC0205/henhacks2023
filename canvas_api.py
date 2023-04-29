#from canvasapi import Canvas
import requests
import datetime
from bakery_canvas import get_courses
import pymongo

API_URL = "https://udel.instructure.com"
API_KEY = "25~dUCIgmpuYNRJDiQ5YFIjRQb5vcSrtWaWBAd1TL1IUfHkvHrbT5BGe4nKNwiEIcfK"

courses = get_courses(API_KEY)

def print_courses(courses):
    for course in courses:
       print(course.name) 
    return
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

#print_courses(courses)
print(current_courses(courses))