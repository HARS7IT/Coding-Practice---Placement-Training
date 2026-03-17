#Encapsulation:
class ATM:
    def __init__(self):
     self.name="Harshit"
     self.card="HDFC"
     self.__pin=5261

    def getPin(self):
      return self.__pin
    
    def setPin(self,newPin):
      self.__pin=newPin
      print("PIN is changed")
      print("New PIN is: ",self.__pin)
obj=ATM()
print(obj.name)
print(obj.card)
print(obj.getPin())
obj.setPin(1234)
print(obj.getPin())


