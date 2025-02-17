# cliente.py

class Cliente:
    def __init__(self, id, x, y,servico):
        self.id = id  # ID único do cliente
        self.id_antena = None  # ID da antena associada (inicialmente nenhuma)
        self.x = x  # Localização do cliente no mapa (coordenada x)
        self.y = y  # Localização do cliente no mapa (coordenada y)
        self.servico = servico

    # Métodos Getters e Setters
    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id

    def get_name_antena(self):
        return self.id_antena

    def set_name_antena(self, id_antena):
        self.id_antena = id_antena

    def get_x(self):
        return self.x

    def set_x(self, x):
        self.x = x

    def get_y(self):
        return self.y

    def set_y(self, y):
        self.y = y

    def get_servico(self):
        return self.servico

    def set_servico(self,servico):
        self.servico=servico

    # Método __str__ para representar o cliente como string
    def to_string(self):
        return f"ID: {self.id}\nLocalização (x, y): ({self.x}, {self.y})\nAntena Associada: {self.id_antena if self.id_antena else 'Nenhuma'}"