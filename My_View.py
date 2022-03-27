class My_View:
	
	def showDataTrain(self, img):
		for line in img:
			for column in line:
				print("%d" %column, end = "")
				
	def showDataTarget(self, data_target):
		for line in range(len(data_target)):
			print('\n')
			for column in range(len(data_target[0])):
				print(data_target[line][column])
				if(line == 20):
					print('\n')

	def __ShowOptions__(self):
						option = -1
						print("MENU DA APLICAÇÃO:")
						print("1 - Carregar dados de treinamento do Dataset")
						print("2 - Carregar dados da verdade terrestre ")
						print("3 - Padronizar dados de treinamento como atributos de entrada ")
						print("4 - Padronizar dados da verdade terrestre como atributos alvo")
						print("5 - Executar Algoritmo Random Forest")
						print("6 - Exibir resultados")
						option = input("Digite o valor da operação para executa-la:")
						return int(option)


