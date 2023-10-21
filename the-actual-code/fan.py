
class Fan:

  
  # attributes
  currentRPM = 0
  
  # constructor
  def __init__(self):
    self.currentRPM = 900
  
  # methods
  def startSpinning(self):
    print("Spinning started")
  
  def stopSpinning(self):
    print("Spinning stopped")
  
  def increaseRPM(self, newRPM):
    self.currentRPM = newRPM
    print("Spinning increased to " + str(newRPM) + " RPM")

  def decreaseRPM(self, newRPM):
   print("Spinning decreased to " + str(newRPM) + " RPM")

  def getCurrentRPM(self):
    return self.currentRPM
