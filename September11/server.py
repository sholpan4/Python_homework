import socket

class UDP_Server:

    def __init__(self):
        super().__init__()
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.address = ('localhost', 9900)

    def start(self): 
        self.socket.bind(self.address)
        is_running = True
        while is_running:
            data, addr = self.socket.recvfrom(1024)
            message = data.decode(encoding= "UTF-8")
            print(f'received message from {addr}: {message}')
            if message == "exit":
                is_running = False

    def stop(self, message = 'exit'):
        if message == 'exit':
            return True
        return False
