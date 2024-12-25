# gestor.py
from antena import Antena
from cliente import Cliente
import math

class Gestor:
    def __init__(self):
        self.antenas = []  # Lista de antenas
        self.clientes = []  # Lista de clientes

    # Função para criar uma antena
    def criar_antena(self, id, raio_cobertura, largura_banda_max, x, y):
        antena = Antena(id, raio_cobertura, largura_banda_max, x, y)
        self.antenas.append(antena)
        return antena

    # Função para remover uma antena
    def remover_antena(self, id):
        antena = self.consultar_antena(id)
        if antena:
            self.antenas.remove(antena)
            return True
        return False

    # Função para listar todas as antenas
    def listar_antenas(self):
        return [antena.to_string() for antena in self.antenas]

    # Função para consultar uma antena por ID
    def consultar_antena(self, id):
        for antena in self.antenas:
            if antena.get_id() == id:
                return antena
        return None

    def criar_cliente(self, id_cliente, x, y):
        if id_cliente not in self.clientes:
            cliente = Cliente(id_cliente, x, y)
            self.clientes[id_cliente] = cliente
        else:
            print(f"Cliente {id_cliente} já existe!")

    def remover_cliente(self, id_cliente):
        if id_cliente in self.clientes:
            del self.clientes[id_cliente]
            return True
        return False

    def listar_clientes(self):
        return list(self.clientes.values())

    def consultar_cliente(self, id_cliente):
        return self.clientes.get(id_cliente, None)
     def criar_antena(self, id_antena, raio_cobertura, largura_banda_max, max_clientes, x, y):
        if id_antena not in self.antenas:
            antena = Antena(id_antena, raio_cobertura, largura_banda_max, max_clientes, x, y)
            self.antenas[id_antena] = antena
        else:
            print(f"Antena {id_antena} já existe!")

    def remover_antena(self, id_antena):
        if id_antena in self.antenas:
            del self.antenas[id_antena]
            return True
        return False

    def listar_antenas(self):
        return list(self.antenas.values())

    def consultar_antena(self, id_antena):
        return self.antenas.get(id_antena, None)

    def associar_cliente_a_antena(self, id_cliente, id_antena):
        cliente = self.clientes.get(id_cliente)
        antena = self.antenas.get(id_antena)
        if cliente and antena and antena.pode_associar_cliente():
            antena.associar_cliente(cliente)
            return True
        return False

    def desassociar_cliente_de_antena(self, id_cliente):
        cliente = self.clientes.get(id_cliente)
        if cliente and cliente.antena_associada:
            cliente.antena_associada.desassociar_cliente(cliente)
            return True
        return False

    def inverter_operacionalidade_antena(self, id_antena):
        antena = self.antenas.get(id_antena)
        if antena:
            antena.inverter_operacionalidade()
            return True
        return False

    def adicionar_servicos_cliente(self, id_cliente, servicos):
        cliente = self.clientes.get(id_cliente)
        if cliente:
            for servico in servicos:
                cliente.adicionar_servico(servico)