
import time
import datetime
from sensor import Sensor
from fan import Fan
from database_connection import DatabaseConnection
class Project:
  # class attribute
  startTime = 0
  sensors = []
  fans = []
  databaseConnection = None
  active = False

  # constructor
  def __init__(self):
    self.starTime = time.time()
    sensorA = Sensor()
    self.sensors.append(sensorA)
    sensorB = Sensor()
    self.sensors.append(sensorB)
    fanA = Fan()
    self.fans.append(fanA)
  
  def startSensorSession(self):
    print("Starting sensor session...")
    #currentDatabaseConnection = DatabaseConnection("sensordata.db")
    self.active = True
    self.fans[0].startSpinning()
    
    while self.active:
      time.sleep(1)
      print("Sensor A: " + str(self.sensors[0].getCurrentValue()))
      print("Sensor B: " + str(self.sensors[1].getCurrentValue()))
      print("Fan: " + str(self.fans[0].getCurrentRPM()))
      #currentDatabaseConnection.saveSensorData("sensorA", self.sensors[0].getCurrentValue(), datetime.datetime.now())
      #currentDatabaseConnection.saveSensorData("sensorB", self.sensors[1].getCurrentValue(), datetime.datetime.now())
      #currentDatabaseConnection.saveFanData(self.fans[0].getCurrentRPM(), datetime.datetime.now()
      if(self.sensors[0].getCurrentValue() > 50):
        self.fans[0].increaseRPM(1000)
      if(self.sensors[0].getCurrentValue() < 50):
        self.fans[0].decreaseRPM(1000)

  def stopSensorSession(self):
    self.active = False
    self.sensors[0].stopReading()
    self.sensors[1].stopReading()
    self.fans[0].stopSpinning()
    print("stopped sensor session...")




# The code below will only run if this file is run directly
# It will not run if this file is imported by another file
# which is the case in our project. We import this file in webserver.py and use it there
if __name__ == "__main__":
  myCurrentProject = Project()
  myCurrentProject.startSensorSession()