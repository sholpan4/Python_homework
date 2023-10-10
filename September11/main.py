import sys
from PyQt6.QtWidgets import *
from client import UDP_Client
from server import UDP_Server


if __name__ == "__main__":
    app = QApplication(sys.argv)

    app.start()

    app.exec()