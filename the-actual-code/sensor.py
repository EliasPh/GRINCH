import adafruit_dht
import board
import time

class Sensor:
  """
  A class representing a sensor that reads temperature from a DHT22 sensor.

  Attributes:
  - startTime (float): the time when the sensor was started
  - gpio (int): the GPIO pin number used by the sensor
  - device (adafruit_dht.DHT22): the DHT22 sensor object used by the sensor
  """

  # constructor
  def __init__(self, selectedGPIO):
    """
    Initializes a new instance of the Sensor class.

    Args:
    - selectedGPIO (int): the GPIO pin number to be used by the sensor
    """
    self.starTime = time.time()
    self.gpio = selectedGPIO
    if(selectedGPIO == 4):
      self.device = adafruit_dht.DHT22(board.D4, use_pulseio=False)
      print("GPIO 4 selected")
    else:
      self.device = adafruit_dht.DHT22(board.D3, use_pulseio=False)
      print("GPIO 3 selected")

  # methods
  def getCurrentValue(self):
    """
    Returns the current temperature value read by the sensor.

    Returns:
    - int: the current temperature value read by the sensor
    """
    return self.readGPIO()

  def readGPIO(self):
    """
    Reads the temperature value from the DHT22 sensor.
    The try-except block and "is not None" are used to handle errors that may occur when reading from the sensor.

    Returns:
    - int: the temperature value read from the DHT22 sensor, or -1 if an error occurred
    """
    try:
       currentValue = self.device.temperature
       if currentValue is not None:
        return currentValue
       else:
        return -1
    except:
      return -1

  def stopReading(self):
    """
    Stops reading from the DHT22 sensor.
    """
    print("Reading stopped")
    self.device.exit()

