
from flask import Flask, render_template

app = Flask(__name__)

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

