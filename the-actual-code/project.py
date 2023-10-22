
import time
import datetime
from sensor import Sensor
from fan import Fan
from database_connection import DatabaseConnection
import random
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
    sensorA = Sensor(4)
    self.sensors.append(sensorA)
    sensorB = Sensor(3)
    self.sensors.append(sensorB)
    fanA = Fan()
    self.fans.append(fanA)
  
  def startSensorSession(self):
    print("Starting sensor session...")
    currentDatabaseConnection = DatabaseConnection("sensordata.db")
    currentDatabaseConnection.connect()
    self.active = True
    # self.fans[0].startSpinning()
         
    while self.active:
     
      dateOfReading = datetime.datetime.now().date()     
      momentOfReading = datetime.datetime.now().strftime("%H:%M:%S")
      sensorAValue = self.sensors[0].getCurrentValue()
      sensorBValue = self.sensors[1].getCurrentValue()
      fanValue = self.fans[0].getCurrentSpeed()

      print("-->", dateOfReading,":",momentOfReading, " Sensor A: " + str(sensorAValue)," Sensor B: " + str(sensorBValue)," Fan: " + str(fanValue))

      currentDatabaseConnection.saveSensorDataA("sensorA", sensorAValue, momentOfReading, dateOfReading)
      currentDatabaseConnection.saveSensorDataB("sensorB", sensorBValue, momentOfReading, dateOfReading)
      currentDatabaseConnection.saveFanData(fanValue, momentOfReading)
     
      if(self.sensors[0].getCurrentValue() > 19):
        self.fans[0].increaseSpeed(5)

      if(self.sensors[0].getCurrentValue() < 18):
        self.fans[0].decreaseSpeed(5) 

      time.sleep(1)

  def stopSensorSession(self):
    self.active = False
    self.sensors[0].stopReading()
    self.sensors[1].stopReading()
    # self.fans[0].stopSpinning()
    print("stopped sensor session...")

  def fetchAllDBData(self):
    currentDatabaseConnection = DatabaseConnection("sensordata.db")
    currentDatabaseConnection.connect()
    data = currentDatabaseConnection.getAllData()
    return data


# The code below will only run if this file is run directly
# It will not run if this file is imported by another file
# which is the case in our project. We import this file in webserver.py and use it there
if __name__ == "__main__":
  myCurrentProject = Project()
  myCurrentProject.startSensorSession()