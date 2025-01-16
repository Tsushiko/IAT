from Graph import Graph
from antena import Antena
from File import parse,write
import matplotlib.pyplot as plt

def main():
    g = Graph()

    
    def menu():
        print("\nMenu Principal")
        print("1-Gerir Clientes")
        print("2-Gerir Antenas")
        print("3-Imprimir Grafo")
        print("4-Desenhar Mapa")
        print("5-Imprimir  antenas de Grafo")
        print("6-Imprimir arestas de Grafo")
        print("7-DFS")
        print("8-BFS")
        print("9-A*")
        print("10-Gulosa")
        print("11-Gravar o estado da cidade.")
        print("0-Saír")
    
    def menu_clientes():
        print("\nMenu de Clientes")
        print("1. Criar Cliente")
        print("2. Listar Clientes")
        print("3. Consultar Cliente")
        print("4. Remover Cliente")
        print("5. Voltar ao Menu Principal")


    def menu_antenas():
        print("\nMenu de Antenas")
        print("1. Criar Antena")
        print("2. Listar Antenas")
        print("3. Consultar Antena")
        print("4. Remover Antena")
        print("5. Voltar ao Menu Principal")

    idantena,id_cliente=parse(g)
    saida = -1

    while saida != 0:
     try:
        menu()
        saida = int(input("introduza a sua saida-> "))
        if saida == 0:
            print("A sair...")
        elif saida == 1:  # Gerir Clientes
            while True:
                menu_clientes()
                saida_cliente = input("Escolha uma opção: ")

                if saida_cliente == "1":
                    id_cliente = id_cliente +1
                    x = float(input("Coordenada X: "))
                    y = float(input("Coordenada Y: "))
                    servico = input("Serviço (streaming/chamada/jogos): ")
                    g.criar_cliente(id_cliente, x, y,servico)
                elif saida_cliente == "2":
                    g.listar_clientes()
                elif saida_cliente == "3":
                    id = input("ID do Cliente a consultar: ")
                    g.consultar_cliente(int(id))
                elif saida_cliente == "4":
                    id = input("ID do Cliente a remover: ")
                    g.remover_cliente(int(id))
                elif saida_cliente == "5":
                    break
                else:
                    print("Opção inválida. Tente novamente.")

        elif saida == 2:  # Gerir Antenas
            while True:
                menu_antenas()
                saida_antena = input("Escolha uma opção: ")

                if saida_antena == "1":
                    idantena = idantena + 1
                    print(idantena)
                    name = input("Nome da antena: ")
                    raio = float(input("Raio de Cobertura: "))
                    largura_banda = int(input("Largura de Banda Máxima: "))
                    x = float(input("Coordenada X: "))
                    y = float(input("Coordenada Y: "))
                    g.criar_antena(name,idantena, raio, largura_banda, x, y)
                elif saida_antena == "2":
                    g.listar_antenas()
                elif saida_antena == "3":
                    name = input("Nome da Antena a consultar: ")
                    antena = g.antenas[name]
                    if antena:
                        print(antena.to_string())
                    else:
                        print("Antena não encontrada!")
                elif saida_antena == "4":
                    name = input("ID da Antena a remover: ")
                    g.remover_antena(name)
                elif saida_antena == "5":
                    break
                else:
                    print("Opção inválida. Tente novamente.")
        elif saida == 3:
            print(g.m_graph)
            l = input("prima enter para continuar")
        elif saida ==4:
            g.desenhamapa()
        elif saida == 5:
            print(g.m_graph.keys())
            l = input("prima enter para continuar")
        elif saida == 6:
            print(g.imprime_aresta())
            l = input("prima enter para continuar")
        elif saida == 7:
            inicio = input("antena inicial->")
            fim = input("antena final->")
            print(g.procura_DFS(inicio, fim, path=[], visited=set()))
            l = input("prima enter para continuar")
        elif saida == 8:
            inicio = input("antena inicial->")
            fim = input("antena final->")
            print(g.procura_BFS(inicio, fim))
            l = input("prima enter para continuar")
        elif saida == 9:
            inicio = input("antena inicial->")
            fim = input("antena final->")
            g.atualizar_heuristica(inicio,fim)
            print(g.procura_aStar(inicio, fim))
            l = input("prima enter para continuar")
        elif saida == 10:
            inicio = input("antena inicial->")
            fim = input("antena final->")
            g.atualizar_heuristica(inicio,fim)
            print(g.greedy(inicio, fim))
            l = input("prima enter para continuar")
        elif saida == 11:
            write(g)
            print("Foi gravado com sucesso.")
        else:
            print("Opção inválida. Tente novamente.")
     except ValueError:
        continue


if __name__ == "__main__":
    main()
