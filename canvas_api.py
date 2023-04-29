from canvasapi import Canvas

API_URL = ""
API_KEY = ""

canvas = Canvas(API_URL,API_KEY)

course = canvas.get_course(123456)
course.name
