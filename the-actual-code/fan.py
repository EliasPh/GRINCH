import RPi.GPIO as GPIO
class Fan:

  
  # attributes
  currentSpeed = 0
  FAN_PIN = 18            # BCM pin used to drive PWM fan
  WAIT_TIME = 1           # [s] Time to wait between each refresh
  PWM_FREQ = 25           # [kHz] 25kHz for Noctua PWM control TODO: check if this is correct
  device = None
  # constructor
  def __init__(self):
    GPIO.setmode(GPIO.BOARD)
    self.currentSpeed = 500
    #GPIO.setup(self.FAN_PIN, GPIO.OUT, initial=GPIO.LOW) # ValueError: A different mode has already been set!
    device = GPIO.PWM(self.FAN_PIN,self.PWM_FREQ)
  
  # methods
  def startSpinning(self):
    print("Spinning started")
    self.device.start(0)
  
  def stopSpinning(self):
    print("Spinning stopped")
    self.device.stop()
    GPIO.cleanup()
  
  def increaseSpeed(self, newSpeed):
    self.currentSpeed = self.currentSpeed+newSpeed
    self.device.ChangeDutyCycle(self.currentSpeed)
    print("Spinning increased to " + str(self.getCurrentSpeed()) + " Speed")

  def decreaseSpeed(self, newSpeed):
   self.currentSpeed = self.currentSpeed-newSpeed
   self.device.ChangeDutyCycle(self.currentSpeed)
   print("Spinning decreased to " + str(self.getCurrentSpeed()) + " Speed")

  def getCurrentSpeed(self):
    return self.currentSpeed
