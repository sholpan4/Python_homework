#1. Создайте шесть файлов .py. 
# В каждом файле создайте по одному любому классу. 
# В каждом классе должно быть:
#   * минимум шесть различных свойств;
#   * конструктор, принимающий значения наиболее 
# вариативных свойств;
#   * минимум четыре различных метода для работы с классом.
#   В каждом файле создайте несколько экземпляров 
# класса и продемонстрируйте его рабту.

class Earphone:
    color = " "
    model = " "
    weight = 0
    volume = 0
    bottom = True or False
    charge = 0
        
    def __init__(self, color, model, weight):
        self.color = color
        self.model = model
        self.weight = weight
        
    def __repr__(self) -> str:
        msg = "Earphone color: %s, model: %s, weight: %d gramm." % (self.color, self.model, self.weight)
        return msg    
            
    def play_music(self, bottom):
        bottom = input("Play? ")
        if bottom == "yes":
            print("Playing the music.")
            
    def stop_music(self, bottom):
        bottom = input("If you want to stop music press 'no': ")
        if bottom == "no" or False:
            print("Music is stopped.")
            
    def volume_up(self, volume):
        n = int(input("How loud to rise: (Please enter number from 1 to 100)"))
        if 0 < n <= 60:
            rise = volume + n
            print("Volume: %d" % rise)
        elif 0 < n <= 100:
            rise = volume + n
            print("Volume: %d. Warning! Listening loud is harmful for your ears." % rise)            
        else:
            n > 100
            print("Can't rise volume up!")
            
    def charge(self, charge):
        charge = int(input("Would like to charge till 100% press '100': "))
        if charge == 100:          
            print("Charged 100%")
        else:
            print("Battery is low! 0%")
            
    print("This earphone is ", __name__)
            
earphone_1 = Earphone("black", "Marshall", 461)
#earphone_2 = Earphone("silver", "AirPods Max", 384)

earphone_1.volume_up(0)
#earphone_1.play_music("")
#earphone_2.stop_music("")
#earphone_2.charge(0)

print(earphone_1)
#print(earphone_2)