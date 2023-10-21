
import time


class Sensor:

  # attributes
  currentValue = 0
  startTime = 0

  # constructor
  def __init__(self):
    self.currentValue = 0
    self.starTime = time.time()

  # methods
  def startReading():
    print("Reading started")
  
  def stopReading():
    print("Reading stopped")
  
  def getCurrentValue(self):
    return self.currentValue

