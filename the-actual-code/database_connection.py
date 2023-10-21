
import sqlite3

class DatabaseConnection:
    def __init__(self, database_name):
        self.database_name = database_name

    def __enter__(self):
        self.connection = sqlite3.connect(self.database_name)
        return self.connection

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.commit()
        self.connection.close()

    def saveSensorData(self, sensorData):
        print("Saving sensor data...", sensorData)
           
    def readSensorData(self):
        print("Reading sensor data...")
        return 19812309