import pandas as pd 
import numpy as np

data = pd.read_csv('dataset.csv')

indices_treinamento = list()
indices_teste = list()

#Crio uma lista de indices do tamanho dos dados obtidos no dataset
indices = list(range(len(data)))

#embaralha os indices
# indices = indices[:100000]
np.random.shuffle(indices) 

#Crio as listas vazias X e Y de treino 
x_train  = list()
y_train = list()

#Fatio os indices, pegando apenas 80% do tamanho do dataset neles
# for i in indices[:80000]:
for i in indices[:int(len(data)*0.8)]:
    #Atribuo na variável linha, a linha "i" do dataset. 
    linha = data.iloc[i]
    #Atribuo em x 
    x = np.zeros((7), dtype=np.int32)
    for j in range(7):
        x[j] = linha[j]
    x_train.append(x)
    y_train.append(linha['classe'])

x_test  = list()
y_test = list()
for i in indices[int(len(data)*0.8):]:
# for i in indices[80000:]:
    linha = data.iloc[i]
    x = np.zeros((7), dtype=np.int32)
    for j in range(7):
        x[j] = linha[j]
    x_test.append(x)
    y_test.append(linha['classe'])

np.save('x_train.npy',np.array(x_train))
np.save('x_test.npy',np.array(x_test))
np.save('indices.npy',np.array(indices))
np.save('y_test.npy',np.array(y_test))
np.save('y_train.npy',np.array(y_train))