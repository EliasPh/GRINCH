from flask import Flask, render_template
import datetime

from project import Project

import threading
# Create a Flask Webserver
app = Flask(__name__)
# Configure the Flask Webserver's Routes
# The function that is called when a user visits a specific route must be written directly below the route for now

currentProject = None
currentThread = None

# starting page
@app.route("/")
def index():
   now = datetime.datetime.now()
   timeString = now.strftime("%Y-%m-%d %H:%M")
   templateData = {
      'title' : 'HELLO!',
      'time': timeString,
      'project_running'  : 'no',
      }
   return render_template('index.html', **templateData)

# this route triggers a new session and is called by a button click
@app.route("/startsession")
def startSensorSession():
    currentThread=threading.Thread(target=currentProject.startSensorSession())
    currentThread.start()
    currentProject.startSensorSession()
    templateData = {
      'project_running'  : 'yes',
      }
    return render_template('index.html', **templateData)

@app.route("/stopsession")
def stopSensorSession():
    currentProject.stopSensorSession()
    currentThread._stop()
    templateData = {
      'project_running'  : 'no',
      }
    return render_template('index.html', **templateData)


if __name__ == "__main__":
   currentProject = Project()
   app.run(host='0.0.0.0', port=1337)