from abc import ABC, abstractclassmethod, abstractmethod
class payment(ABC):
    
  @abstractmethod
  def pay(self,amount):
      pass

class UPIPayment(payment):
    def pay (self ,amount):
       print(f"paid {amount} using UPI")

class Cardpayment(payment):
    def pay (self,amount):
      print(f"paid {amount} using Card")
    
upi = UPIPayment()
card = Cardpayment()
upi.pay(500)
card.pay(1000)
    


    
 