
import time
import random
import board
import adafruit_dht
class Sensor:

  # attributes
  currentValue = 0
  startTime = 0
  gpio = 4
  device = None
  # constructor
  def __init__(self, selectedGPIO):
    self.currentValue = 0
    self.starTime = time.time()
    self.gipo = selectedGPIO
    if(selectedGPIO == 4):
      print("GPIO 4 selected")
      self.device = adafruit_dht.DHT22(board.D4)
    else:
      print("GPIO 3 selected")
      self.device = adafruit_dht.DHT22(board.D3)
  # methods

  
  def getCurrentValue(self):
    return self.readGPIO()

  def readGPIO(self):
    print("Reading GPIO")
    return self.device.temperature
  
  def stopReading(self):
    print("Reading stopped")
    self.device.exit()

