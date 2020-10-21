from threading import Thread
from libs.server_lib import Server
from tkinter import Label


class MyThread(Thread):
    def __init__(self, server: Server, label: Label):
        super().__init__()
        self.__server = server
        self.__label = label

    def run(self) -> None:
        self.__server.gui_work(self.__label)
