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

    def receive_messages(self, client_socket):
        while self.running:
            try:
                message = client_socket.recv(1024).decode('utf-8')
                if message:
                    timestamp = time.strftime('%H:%M:%S', time.localtime())
                    print(f'\n[{timestamp}] {message}')
                    print('Вы: ', end='', flush=True)
            except:
                print('\nСоединение прервано!')
                client_socket.close()
                break


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
