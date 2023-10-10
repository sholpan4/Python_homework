import socket

class UDP_Client:
    address = 'lockalhost'
    port = 0

    def __init__(self, address, port):
        super().__init__()
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.address = address
        self.port = port

    # server_addres = ('192.168.110.150', 9900)
    def send(self, message):
        is_running = True
        while is_running:
            message = input('Enter: ')
            self.socket.sendto(message.encode(), self.address)
            if message == 'exit':
                is_running = False
    
    def receive(self, message):
        pass

