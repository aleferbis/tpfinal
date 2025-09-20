import socket
import pickle


class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = "192.168.100.9"
        self.port = 5555
        self.addr = (self.server, self.port)
        self.p = self.connect()

    def getP(self):
        """
                Devuelve el objeto Player inicial recibido del servidor.

                Returns:
                    Player: Objeto Player del cliente.
                """
        return self.p

    def connect(self):
        """
                Conecta el cliente al servidor y recibe el objeto Player inicial.

                Returns:
                    Player: Objeto Player recibido del servidor.
                """
        try:
            self.client.connect(self.addr)
            return pickle.loads(self.client.recv(2048))
        except:
            pass

    def send(self, data):
        """
                Envía un objeto Player al servidor y recibe la información del otro jugador.

                Args:
                    data (Player): Objeto Player local que contiene posición y estado actual.

                Returns:
                    Player: Objeto Player del otro jugador recibido del servidor.

                Raises:
                    socket.error: Si ocurre un error de conexión o envío.
                """
        try:
            self.client.send(pickle.dumps(data))
            return pickle.loads(self.client.recv(2048))
        except socket.error as e:
            print(e)