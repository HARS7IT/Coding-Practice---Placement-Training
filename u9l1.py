#abstraction:

from abc import ABC, abstractmethod
class Bank(ABC):
    @abstractmethod
    def loan():
        pass
    @abstractmethod
    def fixed_deposit():
        pass

class SBI(Bank):
    def loan():
        print("13% ROI")
    def fixed_deposit():
        print("50k")    
      
class HDFC(Bank):
    def loan():
        print("12% ROI")
    def fixed_deposit():
        print("40k")  

hobj=HDFC
hobj.loan()
hobj.fixed_deposit()
