import bakery_canvas
from nicegui import ui

API_KEY = "25~fv839vqvEiETF0SDI16GdTqqMaz6j1Tc6VX2W8Ml215MuAZB0Vs5XUrg3f7msA3O"

def courses(key):
    courses = bakery_canvas.get_courses(key)
    for course in courses:
        ui.label(course.name)
        
