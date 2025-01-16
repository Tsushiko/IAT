# antena.py

class Antena:
    def __init__(self, name,id=-1, raio_cobertura=10, largura_banda_max=20, x=0, y=0):#(self, id, name   raio_cobertura, largura_banda_max, x, y):
        self.id = id
        self.name = str(name)
        self.raio_cobertura = raio_cobertura
        self.largura_banda_max = largura_banda_max
        self.largura_banda_utilizada = 0 ##deverá ser um valor inteiro que retrate a  percentagem de qunata largura de banda está a ser utilizada
        self.lista_antenas_vizinhas = []
        self.lista_clientes = []  # Lista de clientes associados
        self.lista_clientes_chamada = []  # Lista de clientes em chamada
        self.lista_clientes_streaming = []  # Lista de clientes em streaming
        self.lista_clientes_jogos = []  # Lista de clientes jogando
        self.qos = 100  # A QoS começa com 100%
        self.x = x #Posição x no mapa
        self.y = y #Posição y no mapa
 
    # Métodos Getters e Setters
    
    def getVizinhos(self):
        return self.lista_antenas_vizinhas

    def addVizinho(self,vizinho):
        self.lista_antenas_vizinhas.append(vizinho)

    def getId(self):
        return self.id

    def setId(self, id):
        self.id = id

    def __repr__(self):
        return "node " + self.name
    
    def __str__(self):
        return "node " + self.name
    
    def getName(self):
        return self.name
    
    def __eq__(self, other):
        return self.name == other 

    def __hash__(self):
        return hash(self.name)
    
    def get_raio_cobertura(self):
        return self.raio_cobertura

    def set_raio_cobertura(self, raio):
        self.raio_cobertura = raio

    def get_largura_banda_max(self):
        return self.largura_banda_max

    def set_largura_banda_max(self, largura_banda_max):
        self.largura_banda_max = largura_banda_max

    def get_largura_banda_utilizada(self):
        return self.largura_banda_utilizada

    def set_largura_banda_utilizada(self, largura_banda_utilizada):
        self.largura_banda_utilizada = largura_banda_utilizada

    def get_lista_clientes(self):
        return self.lista_clientes

    def set_lista_clientes(self, lista_clientes):
        self.lista_clientes = lista_clientes

    def get_lista_clientes_chamada(self):
        return self.lista_clientes_chamada

    def set_lista_clientes_chamada(self, lista_clientes_chamada):
        self.lista_clientes_chamada = lista_clientes_chamada

    def get_lista_clientes_streaming(self):
        return self.lista_clientes_streaming

    def set_lista_clientes_streaming(self, lista_clientes_streaming):
        self.lista_clientes_streaming = lista_clientes_streaming

    def get_lista_clientes_jogos(self):
        return self.lista_clientes_jogos

    def set_lista_clientes_jogos(self, lista_clientes_jogos):
        self.lista_clientes_jogos = lista_clientes_jogos

    def get_qos(self):
        return self.qos

    def set_qos(self, qos):
        self.qos = qos

    def get_x(self):
        return self.x

    def set_x(self, x):
        self.x = x

    def get_y(self):
        return self.y

    def set_y(self, y):
        self.y = y

    # Função para retornar as informações de estado da antena
    def to_string(self):
        return (f"Name: {self.name}\n"
                f"Id: {self.id}\n "
                f"Raio de Cobertura: {self.raio_cobertura}\n"
                f"Largura de Banda Máxima: {self.largura_banda_max}\n"
                f"Largura de Banda Utilizada: {self.largura_banda_utilizada}\n"
                f"Clientes: {len(self.lista_clientes)}/{self.largura_banda_max}\n"
                f"QoS: {self.qos}%\n"
                f"Localização (x, y): ({self.x}, {self.y})\n"
                f"Lista de Clientes em Chamada: {', '.join([str(cliente.get_id()) for cliente in self.lista_clientes_chamada])}\n"
                f"Lista de Clientes em Streaming: {', '.join([str(cliente.get_id()) for cliente in self.lista_clientes_streaming])}\n"
                f"Lista de Clientes Jogando: {', '.join([str(cliente.get_id()) for cliente in self.lista_clientes_jogos])}\n")