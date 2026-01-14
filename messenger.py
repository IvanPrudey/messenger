import os
import socket
import sys
import time
import threading


class SimpleMessenger:

    def __init__(self):
        self.running = True
        self.host = '127.0.0.1'
        self.port = 5555
        self.nickname = input('введите Ваш никнейм : ')

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')


def main():
    messenger = SimpleMessenger()
    print('аля вотсап:)')
    print('Возможные режимы:')
    print('1. запустить сервер')
    print('2. подключиться к серверу')
    choise = '0'
    while choise not in ('1', '2'):
        choise = input('Выберите режим 1 или 2: ')
    if choise == '1':
        messenger.start_server()
    elif choise == '2':
        messenger.start_client()
    else:
        pass


if __name__ == '__main__':
    main()
