from socket import *
from time import ctime
from tkinter import Label


class Server(object):

    def __init__(self, host: str, port: int):
        self.__host = host
        self.__port = port
        self.__address = (self.__host, self.__port)
        self.__listener = socket(AF_INET, SOCK_STREAM)

    def config(self):
        self.__listener.bind(self.__address)
        self.__listener.listen(15)

    def work(self):
        self.config()
        while True:
            # 1. Ожидание запросов на соединение:
            print('Сервер находится в режиме ожидания запросов на соединение ...')
            conn, client = self.__listener.accept()
            print(f'{ctime()}: получен запрос на соединение от {client}')

            # 2. Получение исходного сообщения от клиента:
            data = conn.recv(1024)
            mess = bytes.decode(data)
            print(mess)

            # 3. Отправка подтверждения:
            response = f'Сообщение от клиента: [{mess}] - успешно доставлено'
            data = str.encode(response)
            conn.send(data)

            # 4. Закрытие соединения:
            conn.close()
            if mess == 'STOP_SERVER_01012000':
                print('Сервер остановлен по команде администратора')
                break

    def gui_work(self, label: Label):
        self.config()

        def _append_label_text(new_text: str):
            current_text = label.cget('text')
            current_text += '>>> ' + new_text + '\n'
            label.configure(text=current_text)

        while True:
            # 1. Ожидание запросов на соединение:

            # print('Сервер находится в режиме ожидания запросов на соединение ...')
            _append_label_text('Сервер находится в режиме ожидания запросов на соединение ...')
            conn, client = self.__listener.accept()
            # print(f'{ctime()}: получен запрос на соединение от {client}')
            _append_label_text(f'{ctime()}: получен запрос на соединение от {client}')

            # 2. Получение исходного сообщения от клиента:
            data = conn.recv(1024)
            mess = bytes.decode(data)
            print(mess)
            _append_label_text(mess)

            # 3. Отправка подтверждения:
            response = f'Сообщение от клиента: [{mess}] - успешно доставлено'
            data = str.encode(response)
            conn.send(data)

            # 4. Закрытие соединения:
            conn.close()
            if mess == 'STOP_SERVER_01012000':
                print('Сервер остановлен по команде администратора')
                break
