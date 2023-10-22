import time
import datetime
from sensor import Sensor
from fan import Fan
from database_connection import DatabaseConnection

class Project:
  """
  A class representing a project that collects data from sensors and saves it to a database.

  Attributes:
  - startTime (int): the start time of the project
  - sensors (list): a list of Sensor objects
  - fans (list): a list of Fan objects
  - databaseConnection (DatabaseConnection): a DatabaseConnection object
  - active (bool): a flag indicating whether the sensor session is active or not

  Methods:
  - __init__(): constructor method that initializes the sensors and fans
  - startSensorSession(): starts the sensor session and saves the data to the database
  - stopSensorSession(): stops the sensor session and stops the sensors from reading
  - fetchAllDBData(): fetches all the data from the database
  """

  # class attribute
  startTime = 0
  sensors = []
  fans = []
  databaseConnection = None
  active = False

  # constructor
  def __init__(self):
    """
    Initializes the sensors and fans.
    """
    self.starTime = time.time()
    sensorA = Sensor(4)
    self.sensors.append(sensorA)
    sensorB = Sensor(3)
    self.sensors.append(sensorB)
    fanA = Fan()
    self.fans.append(fanA)
  
  def startSensorSession(self):
    """
    Starts the sensor session and saves the data to the database.
    """
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
      currentDatabaseConnection.saveFanData(fanValue, momentOfReading,dateOfReading)
     
      if(self.sensors[0].getCurrentValue() > 19):
        self.fans[0].increaseSpeed(5)

      if(self.sensors[0].getCurrentValue() < 18):
        self.fans[0].decreaseSpeed(5) 

      time.sleep(1)

  def stopSensorSession(self):
    """
    Stops the sensor session and stops the sensors from reading.
    """
    self.active = False
    self.sensors[0].stopReading()
    self.sensors[1].stopReading()
    # self.fans[0].stopSpinning()
    print("stopped sensor session...")

  def fetchAllDBData(self):
    """
    Fetches all the data from the database.

    Returns:
    - data (list): a list of dictionaries containing the data from the database
    """
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