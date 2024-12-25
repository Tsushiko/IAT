# antena.py

class Antena:
    def __init__(self, id, raio_cobertura, largura_banda_max, x, y):
        self.id = id
        self.raio_cobertura = raio_cobertura
        self.largura_banda_max = largura_banda_max
        self.largura_banda_utilizada = 0
        self.lista_clientes = []  # Lista de clientes associados
        self.lista_clientes_chamada = []  # Lista de clientes em chamada
        self.lista_clientes_streaming = []  # Lista de clientes em streaming
        self.lista_clientes_jogos = []  # Lista de clientes jogando
        self.operacional = True  # Inicialmente a antena está operacional
        self.qos = 100  # A QoS começa com 100%
        self.x = x  # Posição x no mapa
        self.y = y  # Posição y no mapa
        self.distancia_cliente_estacaobase = {}  # Dicionário de distâncias dos clientes

    # Métodos Getters e Setters
    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id

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

    def get_operacional(self):
        return self.operacional

    def set_operacional(self, operacional):
        self.operacional = operacional

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

    def get_distancia_cliente_estacaobase(self):
        return self.distancia_cliente_estacaobase

    def set_distancia_cliente_estacaobase(self, cliente_id, distancia):
        self.distancia_cliente_estacaobase[cliente_id] = distancia

    # Função para retornar as informações de estado da antena
    def to_string(self):
        return (f"ID: {self.id}\n"
                f"Raio de Cobertura: {self.raio_cobertura}\n"
                f"Largura de Banda Máxima: {self.largura_banda_max}\n"
                f"Largura de Banda Utilizada: {self.largura_banda_utilizada}\n"
                f"Clientes: {len(self.lista_clientes)}/{self.largura_banda_max}\n"
                f"Estado Operacional: {'On' if self.operacional else 'Off'}\n"
                f"QoS: {self.qos}%\n"
                f"Localização (x, y): ({self.x}, {self.y})\n"
                f"Lista de Clientes em Chamada: {', '.join([str(cliente) for cliente in self.lista_clientes_chamada])}\n"
                f"Lista de Clientes em Streaming: {', '.join([str(cliente) for cliente in self.lista_clientes_streaming])}\n"
                f"Lista de Clientes Jogando: {', '.join([str(cliente) for cliente in self.lista_clientes_jogos])}\n")