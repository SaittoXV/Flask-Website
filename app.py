from flask import Flask, render_template
import mysql.connector

# Creating a flask instance name 'app'
app = Flask(__name__)

# Configuration settings for connecting to the MYSQL database
databaseConnection = mysql.connector.connect(
    host = "TestedJourneys.mysql.pythonanywhere-services.com",
    user = "TestedJourneys",
    password = "Test123!",
    database = "TestedJourneys$default"
)

# Create Database Connection
myCursor = databaseConnection.cursor()

# Check Table Exist
found = False
myCursor.execute("SHOW TABLES")
for table in myCursor:
    print(table[0])
    print(found)
    if table[0] == "todo":
        found = True
        print("The table already exist.")
    else:
        print("The table was not found.")

# Create Table if does not exist
if found == False:
    myCursor.execute("CREATE TABLE todo (id INT NOT NULL, task VARCHAR(255), PRIMARY KEY(id))")
else:
    print("Does not need to create table.")

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

