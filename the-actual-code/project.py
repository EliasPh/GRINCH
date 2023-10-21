
import time
import datetime
from sensor import Sensor
from fan import Fan
from database_connection import DatabaseConnection
class Project:
  # class attribute
  startTime = 0

  # constructor
  def __init__(self):
    self.starTime = time.time()

  def startSensorSession():
    print("Starting sensor session...")
    sensor = Sensor()
    fan = Fan()
    currentDatabaseConnection = DatabaseConnection("sensordata.db")
    currentDatabaseConnection.saveSensorData("test")
    currentDatabaseConnection.readSensorData()
    sensor.startReading()
    fan.startSpinning()
    sensor.stopReading()
    fan.stopSpinning()

  def stopSensorSession():
    print("stopped sensor session...")




# The code below will only run if this file is run directly
# It will not run if this file is imported by another file
# which is the case in our project. We import this file in webserver.py and use it there
if __name__ == "__main__":
  myCurrentProject = Project()
  myCurrentProject.startSensorSession()