from flask import Flask, render_template
import mysql.connector

# Creating a flask instance name 'app'
app = Flask(__name__)

# Configuration settings for connecting to the MYSQL database
databaseConnection = mysql.connector.connect(
    host = "TestedJourneys.mysql.pythonanywhere-services.com"
    user = "TestedJourneys"
    password = "Test123!"
    database = "TestedJourneys$default"
)

# 'MySQL' object from 'flask_mysql' extension is initialize with the flask app, creating a MYSQL connection
mysql = MySQL(app)

class Todo(mysql.model):
    id = mysql.column(mysql.Integer,primary_key= True)
    content = mysql.column(mysql.String(200), nullable = False)
    


@app.route('/')
def homePage():
    return render_template("index.html")

@app.route('/Projects')
def projectPage():
    return render_template("project.html")

@app.route('/Projects/Task Tracker')
def taskTrackerPage():
    return render_template("task_tracker.html")

@app.route('/Games')
def gamePage():
    return render_template("game.html")


if __name__ == "__main__":
    app.run

