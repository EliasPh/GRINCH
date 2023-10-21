
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
      self.device = adafruit_dht.DHT22(board.D4, use_pulseio=False)
      print("GPIO 4 selected")
    else:
      self.device = adafruit_dht.DHT22(board.D3, use_pulseio=False)
      print("GPIO 3 selected")
  # methods

  
  def getCurrentValue(self):
    return self.readGPIO()

  def readGPIO(self):
    print("Reading GPIO")
    try:
       return self.device.temperature
    except:
      return -1
   


  def stopReading(self):
    print("Reading stopped")
    self.device.exit()

