import sys

from PyQt6.QtWidgets import *
#     (
#     QApplication,
#     QGridLayout,
#     QPushButton,
#     QWidget,
# )

class SimpleCalcView(QWidget):
    main_display: QLabel = None

    def on_button_pressed(self):
        
    def __init__(self):
        super().__init__()
        central_widget = QWidget()
        main_layout = QVBoxLayout(central_widget)
        self.setLayout(main_layout)

        result_label = QLabel("0")
        main_layout.addWidget(result_label)

        # self.main_display = QLabel(text='0')
        # # self.main_display.setFont(QFont('Monospace', 20, QFont.Weight.Normal, False))
        # # self.main_display.setAlignment(Qt.AlignmentFlag.AlignRight)
        # main_layout.addWidget(self.main_display)

        app = QApplication([])
        window = QWidget()
        window.setWindowTitle("Calculator")

        layout = QGridLayout()
        layout.addWidget(QPushButton("AC"), 0, 1)
        layout.addWidget(QPushButton("C"), 0, 2)
        layout.addWidget(QPushButton("%"), 0, 3)
        layout.addWidget(QPushButton("/"), 0, 4)

        layout.addWidget(QPushButton("7"), 1, 1)
        layout.addWidget(QPushButton("8"), 1, 2)
        layout.addWidget(QPushButton("9"), 1, 3)
        layout.addWidget(QPushButton("*"), 1, 4)

        layout.addWidget(QPushButton("4"), 2, 1)
        layout.addWidget(QPushButton("5"), 2, 2)
        layout.addWidget(QPushButton("6"), 2, 3)
        layout.addWidget(QPushButton("-"), 2, 4)

        layout.addWidget(QPushButton("3"), 3, 1)
        layout.addWidget(QPushButton("2"), 3, 2)
        layout.addWidget(QPushButton("1"), 3, 3)
        layout.addWidget(QPushButton("+"), 3, 4)

        layout.addWidget(QPushButton("0"), 4, 1, 1, 2)
        layout.addWidget(QPushButton(","), 4, 3)
        layout.addWidget(QPushButton("="), 4, 4)

        main_layout.addLayout(layout)

        window.setLayout(main_layout)

        window.show()
        # sys.exit(app.exec())
        app.exec()

    def set_model(self, model):
        self.calc_model = model
        self.main_layout.setText(model.get_display)