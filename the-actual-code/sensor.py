
import time
import random
import Adafruit-DHT
class Sensor:

  # attributes
  currentValue = 0
  startTime = 0
  type = Adafruit-DHT.DHT22
  gpio = 4
  # constructor
  def __init__(self, selectedGPIO):
    self.currentValue = 0
    self.starTime = time.time()
    self.gipo = selectedGPIO

  # methods

  
  def getCurrentValue(self):
    return self.readGPIO()

  def readGPIO(self):
    humidity = Adafruit-DHT.read_retry(self.type, self.gipo)[0]
    temperature = Adafruit-DHT.read_retry(self.type, self.gipo)[1]
    return temperature
