from tkinter import *
from socket import *
from libs.server_lib import Server
from libs.threads_lib import MyThread


class ServerWindow(object):

    def __init__(self):
        self.__root = Tk()
        self.__frame = Frame(self.__root)
        self.__label = Label(self.__frame)
        self.__chat = Label(self.__frame)
        # chosen ip ->
        # self.__host = gethostbyname(gethostname())
        # self.__host = [(s.connect(('8.8.8.8', 53)), s.getsockname()[0], s.close())
        #                for s in [socket(AF_INET, SOCK_DGRAM)]][0][1]
        self.__host = "127.0.0.1"
        self.__port = 9001
        self.__server = Server(self.__host, self.__port)
        self.__server_thread = MyThread(self.__server, self.__chat)

    def config(self):
        self.__root.title('Серверный модуль')
        self.__root.geometry('700x900')
        self.__root.resizable(True, False)
        self.__label.config(text=str(self.__host), font='Arial 13', fg='purple', )

        self.__chat.config(font='Arial 12', fg='navy', height=20, justify=LEFT, width=100)

    def layout(self):
        self.__frame.pack(padx=15, pady=15)
        self.__label.pack(padx=15)
        self.__chat.pack(pady=15)

    def open(self):
        self.config()
        self.layout()
        self.__server_thread.daemon = True
        self.__server_thread.start()
        self.__root.mainloop()
