import datetime
from flask import Flask, render_template, send_file
from project import Project
import threading
import csv

# Create a Flask Webserver
app = Flask(__name__)
# Configure the Flask Webserver's Routes
# The function that is called when a user visits a specific route must be written directly below the route for now

currentProject = None
currentBackgroundThread = None

# starting page
@app.route("/")
def index():
   now = datetime.datetime.now()
   timeString = now.strftime("%Y-%m-%d %H:%M")
   templateData = {
      'title' : 'Uni Projekt A',
      'time': timeString,
      'project_running'  : 'no',
      }
   return render_template('index.html', **templateData)

# this route triggers a new session and is called by a button click
@app.route("/startsession")
def startSensorSession():
      """
      Starts a sensor session in a separate thread and returns the rendered index.html template with the current time and project status.
      """
      global currentBackgroundThread
      # Start the sensor session in a separate thread
      currentBackgroundThread = threading.Thread(target=currentProject.startSensorSession)
      currentBackgroundThread.daemon = True  # This will allow the thread to exit when the main application exits
      currentBackgroundThread.start()
      now = datetime.datetime.now()
      timeString = now.strftime("%Y-%m-%d %H:%M")
      templateData = {
         'title' : 'Uni Projekt A',
         'time': timeString,
         'project_running'  : 'yes',
         }
      return render_template('index.html', **templateData)

@app.route("/stopsession")
def stopSensorSession():
   global currentBackgroundThread
   if currentBackgroundThread:
      currentProject.stopSensorSession()
      currentBackgroundThread.join()  # Wait for the thread to finish
      currentBackgroundThread = None
   now = datetime.datetime.now()
   timeString = now.strftime("%Y-%m-%d %H:%M")
   templateData = {
   'title' : 'Uni Projekt A',
   'time': timeString,
   'project_running'  : 'no',
   }
   return render_template('index.html', **templateData)

@app.route("/view/data")
def renderData():
   dataFromDB = currentProject.fetchAllDBData()
   
   now = datetime.datetime.now()
   timeString = now.strftime("%Y-%m-%d %H:%M")
   templateData = {
   'title' : 'Uni Projekt A',
   'time': timeString,
      'project_running'  : 'check main page',
      'data':dataFromDB
      }
   return render_template('data.html', **templateData)

@app.route("/createcsv")
def createCSV():

    dataFromDB = currentProject.fetchAllDBData()
    now = datetime.datetime.now()
    timeString = now.strftime("%Y-%m-%d %H:%M")

    with open('sensordata.csv', 'w', newline='') as f:
      writer = csv.writer(f)
      writer.writerow(['Date','Time', 'SensorA', 'SensorB', 'Fan'])
      writer.writerows(dataFromDB)

    templateData = {
    'title' : 'Uni Projekt A',
    'time': timeString,
       'project_running'  : 'check main page',
       'data':dataFromDB
       }
    return render_template('data.html', **templateData)

@app.route("downloadcsv")
def downloadCSV():
    return send_file('sensordata.csv',
                     mimetype='text/csv',
                     attachment_filename='sensordata.csv',
                     as_attachment=True)


if __name__ == "__main__":
   currentProject = Project()
   app.run(host='0.0.0.0', port=1337)