
import sqlite3

class DatabaseConnection:

    connection: None
    cursor: None

    def __init__(self, database_name):
        self.database_name = database_name
        

    def connect(self):
        self.connection = sqlite3.connect(self.database_name)
        self.cursor = self.connection.cursor()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.commit()
        self.connection.close()

    def saveSensorData(self,sensorName,  sensorData, momentOfReading, dateOfReading):
        #self.cursor.execute("INSERT INTO sensorA (temperature, currentdate, currenttime, device) VALUES (?, ?, ?, ?)",(sensorData, currentdate, currenttime, device))
               
        #self.connection.commit()
        print("Saving sensor data...",sensorName,  sensorData, momentOfReading,dateOfReading)
    
    def saveFanData(self, sensorData, momentOfReading,dateOfReading):
        #self.cursor.execute("INSERT INTO fanRPM (fanspeed, currentdate, currenttime, device) VALUES (?, ?, ?, ?)",(sensorData, currentdate, momentOfReading, 'fan'))
               
        print("Saving fan data...", sensorData, momentOfReading,dateOfReading)
           
    def readSensorData(self,sensorName):
        print("Reading sensor data...")
        return 19812309
    
    def readFanData(self):
        print("Reading fan data...")
        return 11111    