
class Fan:

  
  # attributes
  currentRPM = 0
  
  # constructor
  def __init__(self):
    self.currentRPM = 500
  
  # methods
  def startSpinning(self):
    print("Spinning started")
  
  def stopSpinning(self):
    print("Spinning stopped")
  
  def increaseRPM(self, newRPM):
    self.currentRPM = self.currentRPM+newRPM
    print("Spinning increased to " + str(self.getCurrentRPM()) + " RPM")

  def decreaseRPM(self, newRPM):
   self.currentRPM = self.currentRPM-newRPM
   print("Spinning decreased to " + str(self.getCurrentRPM()) + " RPM")

  def getCurrentRPM(self):
    return self.currentRPM
