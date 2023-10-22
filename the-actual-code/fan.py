import board
import pwmio


class Fan:

  
  # attributes
  
  currentSpeed = 0       
  device = None

  # constructor
  def __init__(self):
    self.currentSpeed = 50
    self.device = pwmio.PWMOut(board.D13, frequency=25000, duty_cycle=0)
    print(self.device.duty_cycle)
   
  # methods
  def startSpinning(self):
    print("Spinning started")
    print("Fan: ", self.device)
  
  def stopSpinning(self):
    print("Spinning stopped")
  
  def increaseSpeed(self, i):
    self.device.duty_cycle = int(i * 2 * 65535 / 100)
    self.currentSpeed = self.device.duty_cycle
    print("Spinning increased to " + str(self.getCurrentSpeed()) + "duty_cycle")

  def decreaseSpeed(self, i):
   self.device.duty_cycle = 65535 - int((i - 50) * 2 * 65535 / 100)
   self.currentSpeed = self.device.duty_cycle
   print("Spinning decreased to " + str(self.getCurrentSpeed()) + " duty_cycle")

  def getCurrentSpeed(self):
    return self.currentSpeed
