# main.py
from gestor import Gestor

def menu_cliente(gestor):
    while True:
        print("\nMenu Cliente:")
        print("1. Criar Cliente")
        print("2. Remover Cliente")
        print("3. Listar Clientes")
        print("4. Consultar Cliente")
        print("5. Voltar ao Menu Principal")
        
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            id_cliente = int(input("Digite o ID do Cliente: "))
            x = float(input("Digite a coordenada x do Cliente: "))
            y = float(input("Digite a coordenada y do Cliente: "))
            gestor.criar_cliente(id_cliente, x, y)
            print(f"Cliente {id_cliente} criado com sucesso!")
        
        elif escolha == "2":
            id_cliente = int(input("Digite o ID do Cliente a remover: "))
            if gestor.remover_cliente(id_cliente):
                print(f"Cliente {id_cliente} removido com sucesso!")
            else:
                print("Cliente não encontrado!")

        elif escolha == "3":
            clientes = gestor.listar_clientes()
            if clientes:
                print("\nLista de Clientes:")
                for cliente in clientes:
                    print(cliente)
            else:
                print("Não há clientes registrados.")

        elif escolha == "4":
            id_cliente = int(input("Digite o ID do Cliente a consultar: "))
            cliente = gestor.consultar_cliente(id_cliente)
            if cliente:
                print(cliente.to_string())
            else:
                print("Cliente não encontrado!")

        elif escolha == "5":
            break

        else:
            print("Opção inválida! Tente novamente.")

def menu_antena(gestor):
    while True:
        print("\nMenu Antena:")
        print("1. Criar Antena")
        print("2. Remover Antena")
        print("3. Listar Antenas")
        print("4. Consultar Antena")
        print("5. Associar Cliente a Antena")
        print("6. Desassociar Cliente de Antena")
        print("7. Inverter Operacionalidade da Antena")
        print("8. Voltar ao Menu Principal")
        
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            id_antena = int(input("Digite o ID da Antena: "))
            raio_cobertura = float(input("Digite o raio de cobertura da Antena: "))
            largura_banda_max = float(input("Digite a largura de banda máxima da Antena: "))
            max_clientes = int(input("Digite o número máximo de clientes que a Antena pode suportar: "))
            x = float(input("Digite a coordenada x da Antena: "))
            y = float(input("Digite a coordenada y da Antena: "))
            gestor.criar_antena(id_antena, raio_cobertura, largura_banda_max, max_clientes, x, y)
            print(f"Antena {id_antena} criada com sucesso!")

        elif escolha == "2":
            id_antena = int(input("Digite o ID da Antena a remover: "))
            if gestor.remover_antena(id_antena):
                print(f"Antena {id_antena} removida com sucesso!")
            else:
                print("Antena não encontrada!")

        elif escolha == "3":
            antenas = gestor.listar_antenas()
            if antenas:
                print("\nLista de Antenas:")
                for antena in antenas:
                    print(antena)
            else:
                print("Não há antenas registradas.")

        elif escolha == "4":
            id_antena = int(input("Digite o ID da Antena a consultar: "))
            antena = gestor.consultar_antena(id_antena)
            if antena:
                print(antena.to_string())
            else:
                print("Antena não encontrada!")

        elif escolha == "5":
            id_cliente = int(input("Digite o ID do Cliente: "))
            id_antena = int(input("Digite o ID da Antena: "))
            if gestor.associar_cliente_a_antena(id_cliente, id_antena):
                print(f"Cliente {id_cliente} associado à Antena {id_antena} com sucesso!")

                # Escolher serviços
                print("Escolha os serviços que o cliente irá frequentar (separados por vírgula):")
                print("1. Streaming")
                print("2. Chamada")
                print("3. Jogos")
                servicos = input("Digite os números dos serviços escolhidos: ").split(',')
                servicos = [s.strip() for s in servicos]
                
                # Adicionar o cliente aos serviços escolhidos
                gestor.adicionar_servicos_cliente(id_cliente, servicos)
                print(f"Cliente {id_cliente} associado aos serviços com sucesso!")
            else:
                print("Não foi possível associar o cliente à antena!")

        elif escolha == "6":
            id_cliente = int(input("Digite o ID do Cliente a desassociar: "))
            if gestor.desassociar_cliente_de_antena(id_cliente):
                print(f"Cliente {id_cliente} desassociado com sucesso!")
            else:
                print("Cliente não encontrado ou não está associado a uma antena!")

        elif escolha == "7":
            id_antena = int(input("Digite o ID da Antena para inverter a operacionalidade: "))
            if gestor.inverter_operacionalidade_antena(id_antena):
                print(f"Operacionalidade da Antena {id_antena} invertida com sucesso!")
            else:
                print("Antena não encontrada!")

        elif escolha == "8":
            break

        else:
            print("Opção inválida! Tente novamente.")

def menu_principal(gestor):
    while True:
        print("\nMenu Principal:")
        print("1. Menu Cliente")
        print("2. Menu Antena")
        print("3. Sair")
        
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            menu_cliente(gestor)
        elif escolha == "2":
            menu_antena(gestor)
        elif escolha == "3":
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    gestor = Gestor()  # Instancia o gestor para controlar antenas e clientes
    menu_principal(gestor)  # Chama o menu principal para interação com o usuário