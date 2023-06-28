from random import randint
class Magic:
    magic_type = " "
    lightning = 0
    fire = 0
    wind = 0
    water = " "
    earth = 0
    
    def __init__(self, magic_type, earth = 0):
        self.magic_type = magic_type
        self.earth = randint(-100, 5000)

    
    def __repr__(self) -> str:
        msg = "Magic: %s " % (self.magic_type)
        return msg 
    
    def get_explosion(self, fire, lightning):
        fire = int(input("How much heat you need from 1 to 100? "))
        lightning = int(input("How much volt you need from 1 to 10? "))
        if fire <= 35 and lightning <= 3:
            print("boom~")
        elif 36 <= fire <= 75 and 4 <= lightning <= 7:
            print("BOOOOOM!!!")
        elif 75 <= fire <= 100 and 8 <= lightning <= 10:
            print("BIG BADA BOOOM!!!")
        else:
            print("Please enter number in proposed range!")      
        
    def get_magnetism(self, water, ligthning = 0):
        water = input("To make it rain with thunder press the bottom 'Y' ")            
        if water == "Y" or "y":
            print("Whaaa!!! It's raining with a thunder!")           
        else:
            print("Try more!")
            
    def get_chidori(self, lightning):
        if lightning:
            lightning = lightning ** 2
            print("CHIDORI %d times powerful." % lightning)
            
    def get_cristal(self):
        print(self.earth)
        a = self.earth
        
        if 3500 <= a <= 5000:           
            print("Congratulation! You get a 'Diamond'.")            
        elif 2500 <= a <= 3499:            
            print("Cool! You get a 'Copper'.")            
        elif 1500 <= a <= 2499:            
            print("Not bad. You get a 'Galit'.")            
        elif -100 <= a <= 1499:            
            print("It's a beginning! 'Solid carbon dioxide' also good.")

            
magician_1 = Magic("C4")
magician_1.get_explosion(0, 0)
print(magician_1)

magician_2 = Magic("Uchiha")
magician_2.get_chidori(200)
print(magician_2)