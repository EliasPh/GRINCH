
import time
import random

class Sensor:

  # attributes
  currentValue = 0
  startTime = 0

  # constructor
  def __init__(self):
    self.currentValue = 0
    self.starTime = time.time()

  # methods

  
  def getCurrentValue(self):
    return self.readGPIO()

  def readGPIO(self):
    return random.randint(0, 100)