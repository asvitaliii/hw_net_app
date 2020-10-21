from libs.server_lib import Server
from socket import *
from gui.server_gui import ServerWindow


if __name__ == '__main__':

    server_win = ServerWindow()
    server_win.open()

    # print('Выберите режим запуска сервера:')
    # print('-------------------------------')
    # print('        1 - localhost          ')
    # print('        2 - net                ')
    # print('-------------------------------')
    # print('Ваш выбор? - ')
    # choice = int(input())
    #
    # ip = ''
    # if choice == 1:
    #     ip = '127.0.0.1'
    # elif choice == 2:
    #     # ip = gethostbyname(gethostname())
    #     ip = [(s.connect(('8.8.8.8', 53)), s.getsockname()[0], s.close())
    #           for s in [socket(AF_INET, SOCK_DGRAM)]][0][1]
    # else:
    #     print('Вы выбради неверный вариант')
    #
    # if choice == 1 or choice == 2:
    #     print(f'Сервер запущен с IP: {ip}')
    #     server = Server(ip, 9001)
    #     server.work()
