from PyQt6.QtWidgets import *
from PyQt6.QtCore import pyqtSignal

class CalcControlWidget(QWidget):
    switched : pyqtSignal = None

    def calc_mode_switch(self):
        radiobtn = self.sender()
        if radiobtn.isChecked():
            text = radiobtn.text()
            self.switched.emit(text)
    def __init__(self):
        super().__init__()
        self.switched = pyqtSignal(str)

        central_widget = QWidget()
        main_layout = QVBoxLayout(central_widget)
        self.setLayout(main_layout)

        label = QLabel('Please choose the widget: ')

        rb_simple = QRadioButton('Простой', self)
        rb_simple.setChecked(True)
        rb_simple.toggled.connnect(self.calc_mode_switch)
        main_layout.addWidget(rb_simple)

        rb_account = QRadioButton('Бухгалтерский', self)
        main_layout.addWidget(rb_account)

