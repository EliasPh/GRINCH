import RPi.GPIO as GPIO
class Fan:

  
  # attributes
  
  currentSpeed = 0        #  (0.0 <= dc <= 100.0)
  FAN_PIN = 18            # BCM pin used to drive PWM fan
  WAIT_TIME = 1           # [s] Time to wait between each refresh
  PWM_FREQ = 25           # [kHz] 25kHz for Noctua PWM control TODO: check if this is correct
  device = None

###
###p = GPIO.PWM(channel, frequency)
###To start PWM:
###p.start(dc)   # where dc is the duty cycle (0.0 <= dc <= 100.0)
###To change the frequency:
###p.ChangeFrequency(freq)   # where freq is the new frequency in Hz
###To change the duty cycle:
###p.ChangeDutyCycle(dc)  # where 0.0 <= dc <= 100.0
###To stop PWM:
###p.stop()





  # constructor
  def __init__(self):
    GPIO.setmode(GPIO.BOARD)
    self.currentSpeed = 50
    GPIO.setup(self.FAN_PIN, GPIO.OUT, initial=GPIO.LOW) # ValueError: A different mode has already been set!
    self.device = GPIO.PWM(self.FAN_PIN,self.PWM_FREQ)
  
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
