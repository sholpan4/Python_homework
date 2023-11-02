import sys
from PyQt5.QtCore import Qt, QObject, pyqtSignal, QThread
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QTextEdit, QVBoxLayout, QWidget, QFileDialog

class FileProcessor(QObject):
    finished = pyqtSignal(str)

    def process_file(self, filename):
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
        self.finished.emit(content)

class MainApp(QMainWindow):
    def _init_(self):
        super()._init_()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("File Reader App")
        self.setGeometry(100, 100, 600, 400)

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout(self.central_widget)

        self.text_edit = QTextEdit(self)
        self.layout.addWidget(self.text_edit)

        self.open_button = QPushButton("Открыть", self)
        self.layout.addWidget(self.open_button)

        self.thread = QThread()
        self.file_processor = FileProcessor()
        self.file_processor.moveToThread(self.thread)
        self.thread.started.connect(self.file_processor.process_file)
        self.file_processor.finished.connect(self.display_content)
        self.thread.start()

        self.open_button.clicked.connect(self.open_file)

    def open_file(self):
        file_dialog = QFileDialog(self)
        file_dialog.setFileMode(QFileDialog.ExistingFile)
        file_dialog.setNameFilter("Text files (.txt);;All files ()")

        if file_dialog.exec_():
            selected_file = file_dialog.selectedFiles()[0]
            self.thread.quit()
            self.thread.wait()
            self.thread.start()
            self.thread.started.connect(lambda: self.file_processor.process_file(selected_file))

    def display_content(self, content):
        self.text_edit.setPlainText(content)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_app = MainApp()
    main_app.show()
    sys.exit(app.exec_())