import sys

from PyQt6.QtWidgets import *
#     (
#     QApplication,
#     QGridLayout,
#     QPushButton,
#     QWidget,
# )

class Calc(QWidget):
    main_display: QLabel = None
    def __init__(self):
        super().__init__()
        main_layout = QVBoxLayout()
        self.setLayout(main_layout)

        self.main_display = QLabel(text='0')
        # self.main_display.setFont(QFont('Monospace', 20, QFont.Weight.Normal, False))
        # self.main_display.setAlignment(Qt.AlignmentFlag.AlignRight)
        main_layout.addWidget(self.main_display)

        app = QApplication([])
        window = QWidget()
        window.setWindowTitle("Calculator")

        layout = QGridLayout()
        layout.addWidget(QPushButton("AC"), 0, 1)
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

        window.setLayout(layout)

        window.show()
        sys.exit(app.exec())