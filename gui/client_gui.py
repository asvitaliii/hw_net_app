from PyQt5 import QtWidgets, uic
from libs.client_lib import Client


class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.__win = uic.loadUi('client_window.ui')
        self.__set_win = uic.loadUi('server_settings.ui')
        self.__client: Client = None
        self.__host = None
        self.__port = None

    def __set_slots(self):
        self.__win.set_server_settings.clicked.connect(self.__set_win.show)
        self.__win.ok.clicked.connect(self.send)
        self.__set_win.ok.clicked.connect(self.set_server)

    def show(self):
        self.__set_slots()
        self.__win.show()

    def set_server(self):
        self.__host = self.__set_win.server_ip.text()
        self.__port = self.__set_win.server_port.text()
        self.__win.server_settings.setText(f'Сервер: {self.__host}:{self.__port}')
        self.__client = Client(self.__host, self.__port)
        self.__set_win.close()

    def send(self):
        self.__client.work(self.__win.message.text())
        self.__win.chat.setText(self.__win.chat.text() + self.__client.get_resp())
        self.__win.chat.adjustSize()
