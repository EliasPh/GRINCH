from flask import Flask, render_template
import datetime

from project import Project

# Create a Flask Webserver
app = Flask(__name__)
# Configure the Flask Webserver's Routes
# The function that is called when a user visits a specific route must be written directly below the route for now

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
    currentProject = Project()
    currentProject.startSensorSession()
    templateData = {
      'project_running'  : 'yes',
      }
    return render_template('index.html', **templateData)
# the starting page



if __name__ == "__main__":
   app.run(host='0.0.0.0', port=80, debug=True)