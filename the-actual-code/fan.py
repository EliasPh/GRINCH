import board
import pwmio


class Fan:

  
  # attributes
  
  currentSpeed = 0        #  (0.0 <= dc <= 100.0)
  FAN_PIN = 18            # BCM pin used to drive PWM fan
  WAIT_TIME = 1           # [s] Time to wait between each refresh
  PWM_FREQ = 25           # [kHz] 25kHz for Noctua PWM control TODO: check if this is correct
  device = None






  # constructor
  def __init__(self):
    self.currentSpeed = 50
    self.device = pwmio.PWMOut(board.D13)
   
  
  # methods
  def startSpinning(self):
    print("Spinning started")
    print(self.device)
  
  def stopSpinning(self):
    print("Spinning stopped")
    
  
  def increaseSpeed(self, i):
    self.device.duty_cycle = int(i * 2 * 65535 / 100)
    self.currentSpeed = self.device.duty_clcle
    print("Spinning increased to " + str(self.getCurrentSpeed()) + " Speed")

  def decreaseSpeed(self, i):
   self.device.duty_cycle = 65535 - int((i - 50) * 2 * 65535 / 100)
   self.currentSpeed = self.device.duty_clcle
   print("Spinning decreased to " + str(self.getCurrentSpeed()) + " Speed")

  def getCurrentSpeed(self):
    return self.currentSpeed
