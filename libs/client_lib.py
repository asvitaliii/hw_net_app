from socket import *


class Client(object):
    def __init__(self, host: str, port: int):
        self.__host = host
        self.__port = port
        self.__address = (self.__host, self.__port)
        self.__client = None
        self.__resp = ''

    def connect(self):
        if self.__client is None:
            self.__client = socket(AF_INET, SOCK_STREAM)
            self.__client.connect(self.__address)

    def work(self, mess):
        try:
            self.__resp = ''
            # 1. Отправка начального сообщения:
            data = str.encode(mess)
            self.connect()
            self.__client.send(data)
            self.__resp = self.__resp + f'Сообщение {mess} отправлено\n'

            # 2. Получение ответа сервера:
            data = self.__client.recv(1024)
            response = bytes.decode(data)
            self.__resp = self.__resp + response + '\n'

            # 3. Отключение от сервера:
            self.__client.close()
            self.__client = None

        except Exception as err:
            print(f'Ошибка соединения: {err}')

    def get_resp(self):
        return self.__resp
