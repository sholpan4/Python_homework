import socket

class UDP_Server:

    my_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def __init__(self, port) -> None:
        self.port = port

    def start(self):

        my_addres = ('localhost', 9900)
        my_socket.bind(my_addres)

        is_running = True
        while is_running:
            data, addr = my_socket.recvfrom(1024)
            message = data.decode(encoding= "UTF-8")
            print(f'получено сообщение от {addr}: {message}')
            if message == "exit":
                is_running = False

    def stop(self, message = 'exit'):
        if message == 'exit':
            return True
        return False
