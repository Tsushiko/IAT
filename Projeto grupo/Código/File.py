import re
def parse(grafo):
	id_antena=0
	id_cliente=0
	with open("save.txt", 'r') as ficheiro:
		try:
			for linha in ficheiro:
										   	#nome          raio   largurabanda    x         y
				antena = re.search(r"antena_([A-Za-z0-9]+)_([0-9.]+)_([0-9]+)_([0-9.]+)_([0-9.]+)\n", linha)

				if antena:
					id_antena+=1
					grafo.criar_antena(antena.group(1),id_antena,float(antena.group(2)),int(antena.group(3)),float(antena.group(4)),float(antena.group(5)))
					continue
										   	 	#id 	  x	        y       serviço
				cliente = re.search(r"cliente_([0-9]+)_([0-9.]+)_([0-9.]+)_([A-Za-z]+)([\n]*)", linha)

				if cliente:
					grafo.criar_cliente(int(cliente.group(1)),float(cliente.group(2)),float(cliente.group(3)),cliente.group(4))
					id_cliente=int(cliente.group(1))
		except FileNotFoundError:
			print("O ficheiro de texto save não existe no folder Save")

	#-1 em ambos porque estas variavéis são incrementadas sempre que escolhemos a opção de criar
	return id_antena,id_cliente

def write(grafo):
	with open("save.txt", 'w') as file:
		for antena in grafo.getantenas().values():
			linha = f"antena_{antena.getName()}_{antena.get_raio_cobertura()}_{antena.get_largura_banda_max()}_{antena.get_x()}_{antena.get_y()}\n"
			file.write(linha)


		# Linha para separar
		file.write("\n")
        

		for cliente in grafo.getclientes().values():
			line = f"cliente_{cliente.get_id()}_{cliente.get_x()}_{cliente.get_y()}_{cliente.get_servico()}\n"
			file.write(line)