import pwmio
import board

class Fan:
  """
  A class used to represent a Fan.

  ...

  Attributes
  ----------
  currentSpeed : int
    the current speed of the fan
  device : PWMOut
    the PWMOut device used to control the fan

  Methods
  -------
  startSpinning():
    Starts the fan spinning
  stopSpinning():
    Stops the fan from spinning
  increaseSpeed(i):
    Increases the speed of the fan by i percent
  decreaseSpeed(i):
    Decreases the speed of the fan by i percent
  getCurrentSpeed():
    Returns the current speed of the fan
  """

  currentSpeed = 0       
  device = None

  def __init__(self):
    """
    Constructs all the necessary attributes for the Fan object.

    Parameters
    ----------
    None
    """
    self.currentSpeed = 50
    self.device = pwmio.PWMOut(board.D13, frequency=25000, duty_cycle=0)
    print(self.device.duty_cycle)

  def startSpinning(self):
    """
    Starts the fan spinning.

    Parameters
    ----------
    None
    """
    print("Spinning started")
    print("Fan: ", self.device)

  def stopSpinning(self):
    """
    Stops the fan from spinning.

    Parameters
    ----------
    None
    """
    print("Spinning stopped")

  def increaseSpeed(self, i):
    """
    Increases the speed of the fan by i percent.

    Parameters
    ----------
    i : int
      The percentage by which to increase the fan speed.

    Returns
    -------
    None
    """
    self.device.duty_cycle = int(i * 2 * 65535 / 100)
    self.currentSpeed = self.device.duty_cycle
    print("Spinning increased to " + str(self.getCurrentSpeed()) + "duty_cycle")

  def decreaseSpeed(self, i):
    """
    Decreases the speed of the fan by i percent.

    Parameters
    ----------
    i : int
      The percentage by which to decrease the fan speed.

    Returns
    -------
    None
    """
    self.device.duty_cycle = 65535 - int((i - 50) * 2 * 65535 / 100)
    self.currentSpeed = self.device.duty_cycle
    print("Spinning decreased to " + str(self.getCurrentSpeed()) + " duty_cycle")

  def getCurrentSpeed(self):
    """
    Returns the current speed of the fan.

    Parameters
    ----------
    None

    Returns
    -------
    int
      The current speed of the fan.
    """
    return self.currentSpeed
