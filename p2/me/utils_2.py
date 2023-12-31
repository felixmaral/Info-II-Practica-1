import socket
import random
import time


class Partida:
    def __init__(self, sock1, sock2, n1, n2, id_p):
        self.sockets = [sock1, sock2]
        self.names = [n1, n2]
        self.id = id_p
        self.equipo1 = []
        self.equipo1 = []

    def tirar_moneda(self):
        moneda = tirar_moneda() # -- Para ver quien elige primero cara o cruz

        # ENV 2
        # RECV 2

        if moneda == 0:
            self.sockets[0].send('1'.encode())
            self.sockets[1].send('0'.encode())
            opc = self.sockets[0].recv(1024).decode()

            resultado = tirar_moneda()

            if int(opc) == resultado:
                empieza = f'El primer turno sera para {self.names[0]}'
                self.sockets[0].send(empieza.encode())
                self.sockets[1].send(empieza.encode())
                turno = 0
            else:
                empieza = f'El primer turno sera para {self.names[1]}'
                self.sockets[0].send(empieza.encode())
                self.sockets[1].send(empieza.encode())
                turno = 1

        elif moneda == 1:
            self.sockets[1].send('1'.encode())
            self.sockets[0].send('0'.encode())
            opc = self.sockets[1].recv(1024).decode()

            resultado = tirar_moneda()

            if int(opc) == resultado:
                empieza = f'El primer turno sera para {self.names[1]}'
                self.sockets[0].send(empieza.encode())
                self.sockets[1].send(empieza.encode())
                turno = 1
            else:
                empieza = f'El primer turno sera para {self.names[0]}'
                self.sockets[0].send(empieza.encode())
                self.sockets[1].send(empieza.encode())
                turno = 0

        time.sleep(2)

        return turno

class Server:
    def __init__(self):
        self.lobby = []
        self.partidas = []
        self.sockets = []
        self.sockets_ping = []

class Cliente:
    def __init__(self, name, sck, sck2):
        self.name = name
        self.socket = sck
        self.socket_ping = sck2
        self.id = 0

def tirar_moneda() -> int:
    numero_aleatorio = random.random()
    if 0 <= numero_aleatorio < 0.5:
        return 0
    elif 0.5 <= numero_aleatorio < 1:
        return 1
def print_puntos():
    for i in range(3):
        print((i+1) * '.')
        time.sleep(1)

def comprobar_conexion(sock,data):
    if not data:
        sock.close()
        return 'close'







