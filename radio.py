class radio:
    color='brown'
    brand='Philips'
    def __init__(self):
        print("Your Radio is ready to be Played")
        print("Colour of my Radio = ",self.color)
        print("Brand of my Radio = ",self.brand)
    def power_led(self,power):
        print("Your Radio Power is ",power)
    def mode(self,mode):
        print("Your Radio mode is set to ",mode)
    def frequency(self,fre):
        print("Your Radio frequency is set to ",fre)
    def volume(self,vol):
        print("Your Radio volume is set to ",vol)
    def destroy(self):
        print("Your Radio Power is OFF")

p1=radio()
p1.power_led('ON')
p1.mode('FM')
p1.frequency(102.2)
p1.volume('8')
p1.destroy()
p1=None

    
    
        
        