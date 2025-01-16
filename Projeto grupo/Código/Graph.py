# Classe grafo para representaçao de grafos,
import math
from queue import Queue
import random
import networkx as nx  # biblioteca de tratamento de grafos necessária para desnhar graficamente o grafo
import matplotlib.pyplot as plt  # idem
from matplotlib.patches import Circle
from antena import Antena
from cliente import Cliente
import numpy as np
import heapq


class Graph:
    # def __init__(self, num_of_antenas, directed=False):
    def __init__(self, directed=False):
        self.antenas = {} 
        self.clientes = {}
        self.m_graph = {}  # dicionario para armazenar os nodos e arestas
        self.m_h = {}  # dicionario para posterirmente armazenar as heuristicas para cada nodo -< pesquisa informada
        
    #############
    #    escrever o grafo como string
    #############
    def __str__(self):
        out = ""
        for key in self.m_graph.keys():
            out = out + "antena" + str(key) + ": " + str(self.m_graph[key]) + "\n"
        return out
    
    # Buscar o dicionário de clientes
    def getclientes(self):
        return self.clientes
    

    ###########################
    # Desenha o mapa
    #########################

    def desenhamapa(self):
        # Tamanho
        fig, ax = plt.subplots(figsize=(8, 8))

        # Axis
        ax.set_facecolor("lightgray")  
        # Fundo
        fig.set_facecolor("gray")      

        # Plot 
        for antena in self.antenas.values():
            # Antena
            ax.scatter(antena.get_x(), antena.get_y(), color="red", s=100)
            ax.text(antena.get_x(), antena.get_y(), f"{antena.getName()}", fontsize=12, color="black")
            circle = Circle((antena.get_x(), antena.get_y()), antena.get_raio_cobertura(), color="gray", alpha=0.2)
            ax.add_patch(circle)

            # Cliente com a sua ligação com a Antena
            for cliente in antena.get_lista_clientes():
                ax.scatter(cliente.get_x(), cliente.get_y(), color="blue", s=100)
                ax.text(cliente.get_x(), cliente.get_y(), f"{cliente.get_id()}", fontsize=12, color="black")
                plt.plot([antena.get_x(), cliente.get_x()], [antena.get_y(), cliente.get_y()], color="green", linestyle="-", linewidth=2)

            # Ligação entre Antenas
            for adjacente, peso in self.m_graph[antena.getName()]:
                antena_adj = self.antenas[adjacente]
                # Desenhar linha de ligação
                plt.plot([antena.get_x(), antena_adj.get_x()], [antena.get_y(), antena_adj.get_y()], color="red", linestyle="-", linewidth=2)
            
                # Calcular o ponto médio da linha
                mid_x = (antena.get_x() + antena_adj.get_x()) / 2
                mid_y = (antena.get_y() + antena_adj.get_y()) / 2
            
                # Adicionar o peso no meio da linha
                ax.text(mid_x, mid_y, f"{peso}", fontsize=10, color="black", ha='center', va='center', bbox=dict(facecolor='white', alpha=0.5, edgecolor='none'))

        ax.set_aspect('equal', adjustable='box')
        ax.set_title("Mapa", fontsize=16, pad=20)

        plt.show()

    #Funções para Antenas
    def criar_antena(self,name, id, raio_cobertura, largura_banda_max, x, y):
        if name in self.antenas:
            print(f"Antena com name {name} já existe.")
        else:
            antena1 =  Antena(name,id,raio_cobertura, largura_banda_max, x, y)
            self.m_graph[antena1.getName()] = []
            self.antenas[name] = antena1
            self.procura_edges(antena1)
            
            print(f"Antena {name} criada com sucesso.{self.antenas[name].to_string()}")

    def listar_antenas(self):
        for antena in self.antenas.values():
            print(antena.to_string())

    def consultar_antena(self, id):
        if id in self.antenas:
            print(self.antenas[id].to_string())
        else:
            print(f"Antena com ID {id} não encontrada.")

    def remover_antena(self, name):

        if name in self.antenas:
            lista_clientes = self.antenas[name].get_lista_clientes() 
            del self.antenas[name]
            for antena_adjacente,antenas in self.m_graph.items():
                for nome_antena, peso in antenas:
                    if name == nome_antena:
                        self.m_graph[antena_adjacente].remove((name,peso)) ## situações onde a mesma é adjacente
            del self.m_graph[name] ##remove a antena do gráfico
            for cliente in lista_clientes:
                cliente.set_name_antena(None)
                self.associar_cliente_a_antena(cliente.get_id(), cliente.get_servico())
            print(f"Antena {name} removida com sucesso.")
        else:
            print(f"Antena com ID {name} não encontrada.")
            
#########################################################################################

# Funções para Clientes
    def criar_cliente(self, id, x, y, servico):
        if id in self.clientes:
            print(f"Cliente com ID {id} já existe.")
        else:
            self.clientes[id] = Cliente(id, x, y,servico)
            # Chamando o método correto
            self.associar_cliente_a_antena(id, servico)
            print(f"Cliente {id} criado com sucesso.")
    
    def listar_clientes(self):
        for cliente in self.clientes.values():
            print(cliente.to_string())

    def consultar_cliente(self, id):
        if id in self.clientes:
            print(self.clientes[id].to_string())
        else:
            print(f"Cliente com ID {id} não encontrado.")

    def remover_cliente(self, id):
        if id in self.clientes:
            cliente = self.clientes[id]
            servico = cliente.get_servico()
            if cliente.get_name_antena():
                print(cliente)
                antena_name = cliente.get_name_antena()
                antena = self.antenas[antena_name]
                print(antena)
                antena.get_lista_clientes().remove(cliente)
                if servico == "streaming":
                    largura_banda_necessaria=4
                    antena.get_lista_clientes_streaming().remove(cliente)
                elif servico == "jogos":
                    largura_banda_necessaria=2
                    antena.get_lista_clientes_jogos().remove(cliente)
                elif servico == "chamada":
                    largura_banda_necessaria =1
                    antena.get_lista_clientes_chamada().remove(cliente)
                antena.set_largura_banda_utilizada(antena.get_largura_banda_utilizada() - largura_banda_necessaria)
                
                self.atualizar_edges(cliente,largura_banda_necessaria,False)
                del self.clientes[id]

            print(f"Cliente {id} removido com sucesso.")
        else:
            print(f"Cliente com ID {id} não encontrado.")
   

    def associar_cliente_a_antena(self, cliente_id, servico):
        if cliente_id not in self.clientes:
            print(f"Cliente com ID {cliente_id} não encontrado.")
            return
        ##relacionar largura de banda com o serviço
        if servico == "streaming":
            largura_banda_necessaria=4
        elif servico == "jogos":
            largura_banda_necessaria=2
        elif servico == "chamada":
            largura_banda_necessaria =1

        cliente = self.clientes[cliente_id]
        antenas_viaveis = []
        antenas_penalizadas= []

        for antena in self.antenas.values():
            distancia = self.calcular_distancia_euclidiana(cliente.get_x(),cliente.get_y(),antena.get_x(),antena.get_y())
            if distancia <= antena.get_raio_cobertura() :
                qos= self.calcular_qos(antena,largura_banda_necessaria)
                if antena.get_qos()>=0 and qos>=0 and qos<20:
                    antenas_penalizadas.append((antena,distancia,qos))
                elif antena.get_qos()>=20 and qos>=20:
                    antenas_viaveis.append((antena, distancia))

        if len(antenas_viaveis) == 0:
            if len(antenas_penalizadas) != 0:
                melhor_antena = None
                melhor_qos = -1
                for antena, distancia, qos in antenas_penalizadas:
                    if qos > melhor_qos:
                        # Atualiza a melhor antena e seu QoS
                        melhor_antena = antena
                        melhor_distancia = distancia
                        melhor_qos = qos

                # Adiciona a melhor antena à lista de antenas viáveis
                antenas_viaveis.append((melhor_antena, melhor_distancia))
            else:
                return print("Nenhuma antena disponível!")

        # Ordenar as antenas viáveis pela menor distância
        antenas_viaveis.sort(key=lambda x: (x[1], x[0].get_largura_banda_utilizada()))

        # Escolher a melhor antena disponível
        melhor_antena = antenas_viaveis[0][0]
        menor_distancia = antenas_viaveis[0][1]

        # Filtrar antenas com a mesma distância mínima
        antenas_com_mesma_distancia = [antena for antena, dist in antenas_viaveis if dist == menor_distancia]

        if len(antenas_com_mesma_distancia) > 1:
            # Escolher a antena com menor largura de banda utilizada
            antenas_com_menor_banda = sorted(antenas_com_mesma_distancia, key=lambda a: a.get_largura_banda_utilizada())

            # Filtrar as antenas que têm a mesma largura de banda utilizada
            menor_banda_utilizada = antenas_com_menor_banda[0].get_largura_banda_utilizada()
            antenas_filtradas = [a for a in antenas_com_menor_banda if a.get_largura_banda_utilizada() == menor_banda_utilizada]

            # Escolher aleatoriamente entre as antenas restantes
            melhor_antena = random.choice(antenas_filtradas)
            
        
        
        ##largura_banda_necessaria = self.calcular_largura_banda(str(servico))
        print(f"\nLargura de banda necessária do serviço {servico}: {largura_banda_necessaria}\n")
        if melhor_antena.get_largura_banda_utilizada() + largura_banda_necessaria > melhor_antena.get_largura_banda_max():
            print(f"A largura de banda disponível na antena {melhor_antena.id} é insuficiente para o serviço.")
            return

        melhor_antena.get_lista_clientes().append(cliente)
        ##colocar um if em caso de passar o máximo ; n alocar o cliente
        melhor_antena.set_largura_banda_utilizada(melhor_antena.get_largura_banda_utilizada() + largura_banda_necessaria)
        melhor_antena.set_qos(self.calcular_qos(melhor_antena, largura_banda_necessaria))
        cliente.set_name_antena(melhor_antena.getName())
        self.atualizar_edges(cliente,largura_banda_necessaria)

        if servico == "streaming":
            melhor_antena.get_lista_clientes_streaming().append(cliente)
        elif servico == "chamada":
            melhor_antena.get_lista_clientes_chamada().append(cliente)
        elif servico == "jogos":
            melhor_antena.get_lista_clientes_jogos().append(cliente)

        
        print(f"Cliente {cliente_id} associado à antena {melhor_antena.id} com sucesso para o serviço {servico}.")

    def calcular_qos(self,melhor_antena, largura_banda_necessaria, flag=True):
        qos_antena = melhor_antena.get_qos()
        diferenca_qos = (largura_banda_necessaria * 100)/melhor_antena.get_largura_banda_max()
        if flag:
            qos=qos_antena - diferenca_qos
        else:
            qos=qos_antena + diferenca_qos
        return qos


################## Arestas ###############################################################
##########################################################################################
    
    def calcular_distancia_euclidiana(self, x1, y1, x2, y2):
        p = [x1, y1]
        q = [x2, y2]
        # Calculate Euclidean distance
        #print(math.dist(p, q))
        return math.dist(p, q)
    def peso(self, antena1, antena2):
        return antena1.get_largura_banda_utilizada() + antena2.get_largura_banda_utilizada() 
       
    def procura_edges(self,antena1):
        if len(list(self.antenas.values()))!=1:
            for antena2 in self.antenas.values():
                distancia= self.calcular_distancia_euclidiana(antena1.get_x(),antena1.get_y(),antena2.get_x(),antena2.get_y())
                if (antena1.getName()!=antena2.getName() and distancia<=antena1.get_raio_cobertura() and distancia<=antena2.get_raio_cobertura()):
                   # print("\nERRO:"+ str(distancia))
                    self.add_edge(antena1,antena2,self.peso(antena1,antena2))
                
    def add_edge(self, antena1, antena2, peso): ##modificar esta função para guardar os valores da largurta de banda e afins
        antena1.addVizinho(antena2.getName())
        antena2.addVizinho(antena1.getName())
        self.m_graph[antena1.getName()].append((antena2.getName(), peso))  
        self.m_graph[antena2.getName()].append((antena1.getName(), peso))

    
    def atualizar_edges(self, cliente, largura_banda_nova, flag=True):
        nome_antena = cliente.get_name_antena()
        arestas_para_atualizar = []


        for adjacente, peso in self.m_graph[nome_antena]:
            if flag:
                novo_peso = peso + largura_banda_nova
            else:
                novo_peso = peso - largura_banda_nova
                antena= self.antenas[nome_antena]
                self.antenas[nome_antena].set_qos(self.calcular_qos(antena, largura_banda_nova, False))

            arestas_para_atualizar.append((adjacente, novo_peso))

        self.m_graph[nome_antena] = arestas_para_atualizar

        for adjacente, novo_peso in arestas_para_atualizar:
            aux = 0
            for (adjacente_bidirecional, peso) in self.m_graph[adjacente]:
                if adjacente_bidirecional == nome_antena:
                    self.m_graph[adjacente][aux] = (nome_antena, novo_peso)
                    break
                aux += 1

        print(f"\n Atualizado: {self.m_graph[nome_antena]}")

        

        
##########################################################################################

    def atualizar_heuristica(self, inicio, fim):
    
    
        # Inicialização do dicionário de distâncias (inicialmente infinito para todos os nós)
        distancias = {nodo: float('inf') for nodo in self.m_graph}
        distancias[fim] = 0  # A distância do nó final até ele mesmo é 0
    
        # Fila de prioridade para processar os nós por ordem de distância
        fila_prioridade = [(0, fim)]
    
        # Processar cada nó na fila de prioridade
        while fila_prioridade:
            dist_atual, nodo_atual = heapq.heappop(fila_prioridade)
        
            # Verificar todos os vizinhos do nodo atual
            for vizinho, peso in self.m_graph[nodo_atual]:
                nova_dist = dist_atual + peso
            
                # Se a nova distância é menor, atualize e adicione à fila
                if nova_dist < distancias[vizinho]:
                    distancias[vizinho] = nova_dist
                    heapq.heappush(fila_prioridade, (nova_dist, vizinho))
    
        # Atualizar a heurística no objeto com base nas distâncias calculadas
        for nodo in self.m_graph:
            self.m_h[nodo] = distancias[nodo]

        return True


    ##############################3
    #   imprimir arestas
    ############################333333

    def imprime_aresta(self):
        listaA = ""
        lista = self.m_graph.keys()
        for nodo in lista:
            for (antena2, custo) in self.m_graph[nodo]:
                listaA = listaA + nodo + " ->" + antena2 + " custo:" + str(custo) + "\n"
        return listaA


    #############################
    # devolver antenas
    ##########################

    def getantenas(self):
        return self.antenas

    #######################
    #    devolver o custo de uma aresta
    ##############

    def get_arc_cost(self, antena1, antena2):
        custoT = math.inf
        a = self.m_graph[antena1]  # lista de arestas para aquele nodo
        for (nodo, custo) in a:
            if nodo == antena2:
                custoT = custo

        return custoT

    ##############################
    #  dado um caminho calcula o seu custo
    ###############################

    def calcula_custo(self, caminho):
        # caminho é uma lista de nodos
        teste = caminho
        custo = 0
        i = 0
        while i + 1 < len(teste):
            custo = custo + self.get_arc_cost(teste[i], teste[i + 1])
            #print(teste[i])
            i = i + 1
        return custo

    ################################################################################
    #     procura DFS
    ####################################################################################

    def procura_DFS(self, start, end, path=[], visited=set()):
        path.append(start)
        visited.add(start)

        if start == end:
            # calcular o custo do caminho funçao calcula custo.
            custoT = self.calcula_custo(path)
            return (path, custoT)
        for (adjacente, peso) in self.m_graph[start]:
            if adjacente not in visited:
                resultado = self.procura_DFS(adjacente, end, path, visited)
                if resultado is not None:
                    return resultado
        path.pop()  # se nao encontra remover o que está no caminho......
        return None

    #####################################################
    # Procura BFS
    ######################################################

    def procura_BFS(self, start, end):
        # definir nodos visitados para evitar ciclos
        visited = set()
        fila = Queue()
        custo = 0
        # adicionar o nodo inicial à fila e aos visitados
        fila.put(start)
        visited.add(start)

        # garantir que o start antena nao tem pais...
        parent = dict()
        parent[start] = None

        path_found = False
        while not fila.empty() and path_found == False:
            nodo_atual = fila.get()
            if nodo_atual == end:
                path_found = True
            else:
                for (adjacente, peso) in self.m_graph[nodo_atual]:
                    if adjacente not in visited:
                        fila.put(adjacente)
                        parent[adjacente] = nodo_atual
                        visited.add(adjacente)

        # reconstruir o caminho

        path = []
        if path_found:
            path.append(end)
            while parent[end] is not None:
                path.append(parent[end])
                end = parent[end]
            path.reverse()
            # funçao calcula custo caminho
            custo = self.calcula_custo(path)
        return (path, custo)

    ####################
    # funçãop  getneighbours, devolve vizinhos de um nó
    ##############################

    def getNeighbours(self, nodo):
        lista = []
        for (adjacente, peso) in self.m_graph[nodo]:
            lista.append((adjacente, peso))
        return lista



    def procura_aStar(self, start, end):
        # open_list is a list of antenas which have been visited, but who's neighbors
        # haven't all been inspected, starts off with the start antena
        # closed_list is a list of antenas which have been visited
        # and who's neighbors have been inspected

        #atualizar_euristicas() criar um função para atualizar as heuisticas de acordo com o objetivo final, o objetivo final deve ser 0
        open_list = {start}
        closed_list = set([])

        # g contains current distances from start_antena to all other antenas
        # the default value (if it's not found in the map) is +infinity
        g = {}  ##  g é apra substiruir pelo peso  ???

        g[start] = 0

        # parents contains an adjacency map of all antenas
        parents = {}
        parents[start] = start
        #n = None
        while len(open_list) > 0:
            # find a antena with the lowest value of f() - evaluation function
            n = None

            # find a antena with the lowest value of f() - evaluation function
            for v in open_list:
                ##if n == None or g[v] + self.getH(v) < g[n] + self.getH(n):  # heuristica ver.....
                if n == None or g[v] + self.getH(v) < g[n] + self.getH(n):  # heuristica ver.....
                    n = v
            if n == None:
                print('Path does not exist!')
                return None

            # if the current antena is the stop_antena
            # then we begin reconstructin the path from it to the start_antena
            if n == end:
                reconst_path = []

                while parents[n] != n:
                    reconst_path.append(n)
                    n = parents[n]

                reconst_path.append(start)

                reconst_path.reverse()

                return (reconst_path, self.calcula_custo(reconst_path))

            # for all neighbors of the current antena do
            for (m, weight) in self.getNeighbours(n):  # definir função getneighbours  tem de ter um par nodo peso
                # if the current antena isn't in both open_list and closed_list
                # add it to open_list and note n as it's parent
                if m not in open_list and m not in closed_list:
                    open_list.add(m)
                    parents[m] = n
                    g[m] = g[n] + weight

                # otherwise, check if it's quicker to first visit n, then m
                # and if it is, update parent data and g data
                # and if the antena was in the closed_list, move it to open_list
                else:
                    if g[m] > g[n] + weight:
                        g[m] = g[n] + weight
                        parents[m] = n

                        if m in closed_list:
                            closed_list.remove(m)
                            open_list.add(m)

            # remove n from the open_list, and add it to closed_list
            # because all of his neighbors were inspected
            open_list.remove(n)
            closed_list.add(n)

        print('Path does not exist!')
        return None

    ###################################3
    # devolve heuristica do nodo
    ####################################

    def getH(self, nodo):
        if nodo not in self.m_h.keys():
            return 1000
        else:
            return (self.m_h[nodo])


    ##########################################
    #   Greedy
    ##########################################


    def greedy(self, start, end):
        # open_list é uma lista de nodos visitados, mas com vizinhos
        # que ainda não foram todos visitados, começa com o  start
        # closed_list é uma lista de nodos visitados
        # e todos os seus vizinhos também já o foram
        open_list = set([start])
        closed_list = set([])

        # parents é um dicionário que mantém o antecessor de um nodo
        # começa com start
        parents = {}
        parents[start] = start

        while len(open_list) > 0:
            n = None

            # encontraf nodo com a menor heuristica
            for v in open_list:
                if n == None or self.m_h[v] < self.m_h[n]:
                    n = v

            if n == None:
                print('Path does not exist!')
                return None

            # se o nodo corrente é o destino
            # reconstruir o caminho a partir desse nodo até ao start
            # seguindo o antecessor
            if n == end:
                reconst_path = []

                while parents[n] != n:
                    reconst_path.append(n)
                    n = parents[n]

                reconst_path.append(start)

                reconst_path.reverse()

                return (reconst_path, self.calcula_custo(reconst_path))
            # para todos os vizinhos  do nodo corrente
            
            for (m, weight) in self.getNeighbours(n):
                # Se o nodo corrente nao esta na open nem na closed list
                # adiciona-lo à open_list e marcar o antecessor
                if m not in open_list and m not in closed_list:
                    open_list.add(m)
                    parents[m] = n


            # remover n da open_list e adiciona-lo à closed_list
            # porque todos os seus vizinhos foram inspecionados
            open_list.remove(n)
            closed_list.add(n)

        print('Path does not exist!')
        return None