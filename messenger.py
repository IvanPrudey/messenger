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
