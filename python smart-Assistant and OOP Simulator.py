import winsound

class Smartphone:
    def __init__(self,brand,storage):
     self.brand = brand
     self.storage = storage
        
    def ring(self):
        print(f"{self.brand} phone is ringing....")
        winsound.Beep(2000, 1000)

phone = Smartphone("samssung", 128)
phone.ring()






             
                                                       
                 
