
class SimpleCalcModel:
    __display = '0'  #hide the display

    def calculate(self):
        try:
            result = eval(self.__display)
            self.__display = str(result)
        except SyntaxError:
            print("Not correct value")

    def command(self, key: str):
        if key != "=":
            if key.isdigit():
                if self.__display == '0':
                    self.__display = key
                else:
                    self.__display += key
            else:
                if self.__display[-1] not in "+-*/":
                    self.__display += key

                else:
                    self.__display += key

            if key == "C":
                if len(self.__display) == 1:
                    self.__display = self.__display
                else:
                    self.__display = self.__display[:-1]

            if key == "AC":
                self.__display = "0"




    def get_display(self):
        return self.__display

if __name__ == '__main__':
    print('Testing model')
    calc = SimpleCalcModel()

    calc.command('3')
    calc.command('+')
    calc.command('7')
    calc.command('=')

    calc.calculate()

    print(calc.get_display())