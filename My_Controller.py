import cv2
import matplotlib
import numpy
from My_View import My_View
from My_Model import My_Model
import sys
import os
sys.path.insert(0, '/classes')

from classes.image import My_Image
from sklearn.ensemble import RandomForestClassifier

class My_Controller:
	def __init__(self):
		self.model = My_Model()
		self.view  = My_View()

#------------------Aquisição dos dados-----------------
	def readDataTrain(self, local, name_files):
		for name in name_files:
			band = name[15:17]
			img = self.readImage((local + name))
			self.saveDataTrain(band, img)
			print("Banda: "+ band + " carregado com sucesso!")

	def readDataTarget(self, local, name_file):
		band = name_file[15:17]
		data = self.readImage((local + name_file))
		self.saveDataTarget(band, data)
		print("Banda: ", band)
		print("Data target carregado com sucesso!")

	def readImage(self, path):
		img = cv2.imread(path, cv2.IMREAD_UNCHANGED)
		return img

	def saveDataTrain(self, band, img):
		self.model.__setCollection__(band, img)

	def saveDataTarget(self, band, img):
		self.model.__setEarthTruth__(band, img)

#-----------------Fim Aquisição de Dados-----------------

#-----------------Tratamento dos Dados-----------------\
	def standardizeDataTrain(self):
		data = self.model.__getCollection__()
		final_data = []
		
		for image in data:
			aux_data = []
			for line in data[image]:
				for column in line:
					aux_data.append(column)
			
			final_data.append(aux_data)
		
		self.model.data_train = final_data

	def standardizeDataTarget(self):
		target = self.model.__getEarthTruth__()
		final_data = []

		for line in target['B1']:
			for column in line:
				if column != -99.0:
					final_data.append(column)

		self.model.data_target = final_data

#-----------------Fim Tratamento dos dados-----------------

#-----------------Executando RF-----------------
	def runRandomForest(self):
		rf = RandomForestClassifier(n_estimators=5, oob_score=False, random_state=0, n_jobs=-1)

		X = self.model.__getDataTrain__()
		y = self.model.__getDataTarget__()

		x_train = [X[0][:100]]
		y_train = [y[:100]]
		print("X_train:", x_train)
		print("Y_Train:", y_train)
		print(len(x_train))
		print("Iniciando função Fit")
		rf.fit(x_train, y_train) 
		print("Modelo contruído!")
		print("Iniciando Predição de B2")
		print(rf.predict([X[1][:100]]))
		print(rf.predict_proba([X[1][:100]]))
		print(rf.score([X[1][:100]], y_train))

#-----------------Fim Execução RF-----------------

#-----------------Iteração com usuário-----------------
	def __RunMenu__(self):
		while True:
			option = self.view.__ShowOptions__()
			self.handleOptions(option)
			os.system("pause")
			self.clearScreen()

	def handleOptions(self, option):
		if option == 1:
			self.readDataTrain(self.model.path, self.model.files_name)
		elif option == 2:
			self.readDataTarget(self.model.path_target, self.model.file_target)
		elif option == 3:
			self.standardizeDataTrain()
			print("Imagens convertidas para Arrays 1D")
		elif option == 4:
			self.standardizeDataTarget()
			print("Imagem convertida para Array 1D")
		elif option == 5: 
			self.runRandomForest()
			print("RF Executado com sucesso!")
		else:
			print("Opção não existe: reentre!")

	def clearScreen(self):
		if os.name == "posix":
			os.system("clear")
		elif os.name in ("nt", "dos", "ce"):
			os.system("CLS")
		else:
			print("Não rolou")
#-----------------Fim da Iteração com usuário-----------------
