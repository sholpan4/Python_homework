
#python3 -m venv .venv
#python3 -m pip install PyQt5
#$Env:QT_QPA_PLATFORM_PLUGIN_PATH = "venv/lib/site-packages/PyQt6/Qt6/plugins/platforms"

import sys
from PyQt6.QtWidgets import QApplication
from calc_main import CalcMainWindow
from calc_view import *
from calc_model import *
from calc_control import CalcControlWidget

def switch_mode(name):
    if name == "Account":
        view = AccountCalcView()
        model = AccountCalcModel()

if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = CalcMainWindow('Calc')
    view = SimpleCalcView()
    model = SimpleCalcModel()
    control = CaclControlWidget()

    window.set_control(control)
    view.set_model(model)
    window.set_view()
    window.show()
    app.execa()