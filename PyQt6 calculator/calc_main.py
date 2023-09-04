from PyQt6.QtWidgets import QMainWindow, QGridLayout, QWidget

class CalcMainWindow(QMainWindow):
    calc_view = None
    calc_layout =None
    def __init__(self, title):
        super().__init__()
        self.setWindowTitle(title)
        main_widget = Qwidget()
        self.calc_layout = QGridLayout()
        self.setLayout(self.calc_layout)
        self.setCenterlWidget(main_widget)
    def set_view(self, view):
        self.calc_view = view
        self.setCentralWidget(self.calc_view, 1, 0)

    def set_model(self, model):
        self.calc_model = model
        if self.calc_view:
            self.calc_view.set_model(model)
    def set_control(self, widget):
        self.calc_control = addWidget(widget, 0, 0)


