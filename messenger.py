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

    def send_message(self, client_socket):
        while self.running:
            try:
                message = input()
                if message.lower() == '/exit':
                    self.running = False
                    client_socket.send(f"{self.nickname} покинул чат".encode('utf-8'))
                    break
                elif message.lower() == '/clear':
                    self.clear_screen()
                    print('-----------------------------------------------------')
                    print('-----------------------------------------------------')
                    print('аля вотсап version_1:)')
                    print("Вы: ", end="", flush=True)
                    continue
                full_message = f'{self.nickname}: {message}'
                client_socket.send(full_message.encode('utf-8'))
            except:
                break

def start_server(self):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((self.host, self.port))
    server.listen()
    print(f'Сервер запущен на {self.host}:{self.port}')
    print('Ожидание подключений...')
    clients = []
    nicknames = []

    def broadcast(message):
        for client in clients:
            try:
                client.send(message.encode('utf-8'))
            except:
                index = clients.index(client)
                clients.remove(client)
                client.close()
                nickname = nicknames[index]
                broadcast(f"{nickname} покинул чат")
                nicknames.remove(nickname)

    def handle_client(client):
        while True:
            try:
                message = client.recv(1024).decode('utf-8')
                if message:
                    broadcast(message)
            except:
                index = clients.index(client)
                clients.remove(client)
                client.close()
                nickname = nicknames[index]
                broadcast(f"{nickname} покинул чат")
                nicknames.remove(nickname)
                break

    def accept_connections():
            while True:
                client, address = server.accept()
                print(f"Новое подключение от {str(address)}")
                client.send("NICK".encode('utf-8'))
                nickname = client.recv(1024).decode('utf-8')
                nicknames.append(nickname)
                clients.append(client)
                print(f"Никнейм клиента: {nickname}")
                broadcast(f"{nickname} присоединился к чату!")
                thread = threading.Thread(target=handle_client, args=(client,))
                thread.start()

    accept_thread = threading.Thread(target=accept_connections)
    accept_thread.start()




def main():
    messenger = SimpleMessenger()
    print('-----------------------------------------------------')
    print('-----------------------------------------------------')
    print('аля вотсап version_1:)')
    print('-----------------------------------------------------')
    print('-----------------------------------------------------')
    print('Возможные режимы:')
    print('1. запустить сервер')
    print('2. подключиться к серверу')
    print('-----------------------------------------------------')
    print('-----------------------------------------------------')
    choise = '0'
    while choise not in ('1', '2'):
        choise = input('Выберите режим 1 или 2: ')
    if choise == '1':
        messenger.start_server()
    elif choise == '2':
        messenger.start_client()
    else:
        pass
    print('-----------------------------------------------------')
    print('-----------------------------------------------------')


if __name__ == '__main__':
    main()
