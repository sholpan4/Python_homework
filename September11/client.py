import socket

class UDP_Client:
    address = 'lockalhost'
    port = 0
    my_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def __init__(self, address, port) -> None:
        self.address = address
        self.port = port

    # server_addres = ('192.168.110.150', 9900)
    def send(self, message):
        is_running = True
        while is_running:
            message = input('Введите что-нибудь(желательно на английском): ')
            my_socket.sendto(message.encode(), server_addres)
            if message == 'exit':
                is_running = False
    
    def receive(self):
        pass

