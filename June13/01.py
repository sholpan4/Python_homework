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
    size = 0
    volume = 0
    bottom = True or False
    charge = 0
    
    
    def play_music(self, bottom):
        bottom = input("Play? ")
        if bottom == "yes" or True:
            print("Playing the music.")
            
    def stop_music(self, bottom):
        bottom = input("Stop?")
        if bottom == "yes" or False:
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
        charge = input("Charge? Yes/No")
        if answer == "Yes":
            print("Charged")
        else:
            print("Battery is low!")
            
earphone_1 = Earphone()
earphone_1.volume_up(70)
print(earphone_1)

earphone