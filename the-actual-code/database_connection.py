
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

    def saveSensorDataA(self,sensorName,  sensorData, momentOfReading, dateOfReading):
        self.cursor.execute("INSERT INTO sensora (temperature, currentdate, currenttime, device) VALUES (?, ?, ?, ?)",(sensorData, dateOfReading, momentOfReading, sensorName))
        self.connection.commit()
        print("Saving sensor data...",sensorName,  sensorData, momentOfReading,dateOfReading)
    
    def saveSensorDataB(self,sensorName,  sensorData, momentOfReading, dateOfReading):
        self.cursor.execute("INSERT INTO sensorb (temperature, currentdate, currenttime, device) VALUES (?, ?, ?, ?)",(sensorData, dateOfReading, momentOfReading, sensorName))
        self.connection.commit()
        print("Saving sensor data...",sensorName,  sensorData, momentOfReading,dateOfReading)
    
    def saveFanData(self, sensorData, momentOfReading,dateOfReading):
        self.cursor.execute("INSERT INTO fan (fanspeed, currentdate, currenttime, device) VALUES (?, ?, ?, ?)",(sensorData, dateOfReading, momentOfReading, 'fan'))
        self.connection.commit()               
        print("Saving fan data...", sensorData, momentOfReading,dateOfReading)
           
    def readSensorAData(self):
        print("Reading sensor A data...")
        self.cursor.execute("SELECT * FROM sensora")
        data = self.cursor.fetchall()
        return data
    
    def readSensorBData(self):
        print("Reading sensor B data...")
        self.cursor.execute("SELECT * FROM sensorb")
        data = self.cursor.fetchall()
        return data
    
    def readFanData(self):
        print("Reading fan data...")
        self.cursor.execute("SELECT * FROM fan")
        data = self.cursor.fetchall()
        return data  