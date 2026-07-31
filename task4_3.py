#task 4.3

import sqlite3
from flask import *

app = Flask(__name__)

conn = sqlite3.connect('school.db')
cursor = conn.execute("SELECT ScreenName FROM People")
rows = cursor.fetchall()

screen_name = []
for row in rows:
    screen_name.append(row)

with open('people.txt' , 'r') as file:
    lines = file.read().strip().split('\n')
    data = []
    for i in range(len(lines)):
        parts = lines[i].split(',')
        full_name = parts[0].strip()
        role = parts[2].strip()
        current_screen_name = screen_name[i][0]

        if role == "Staff":
            identity = "staff"
        elif role == "Student":
            identity = "student"
        else:
            identity = "person"

        data.append([full_name , current_screen_name, identity])

@app.route('/')
def index():
    return render_template('index.html' , data = data)
app.run(port = 5000)

        
    




        
