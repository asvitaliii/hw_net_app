import sys
from PyQt5.QtWidgets import QApplication
from gui.client_gui import Window


if __name__ == '__main__':
    app = QApplication([])
    client = Window()
    client.show()
    sys.exit(app.exec())
