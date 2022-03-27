import numpy as np 
import pandas as pd
from datetime import datetime as dt
from sklearn.ensemble import RandomForestClassifier

data = pd.read_csv('dataset.csv')
print(data['classe'].value_counts())

x_test = np.load('x_test.npy')
y_test = np.load('y_test.npy')

x_train = np.load('x_train.npy')
y_train = np.load('y_train.npy')

rf = RandomForestClassifier(n_estimators=200, random_state=0, n_jobs=-1, class_weight = 'balanced')
print("Início do treinamento...")
inicio = dt.now()
rf.fit(x_train, y_train)
print("Fim  do treinamento: ", dt.now() - inicio)

print("Classes:", rf.classes_)
print("Número de classes:", rf.n_classes_)
print("Predição das classes: ", rf.predict(x_test))
print("Acurácia obtida: ", rf.score(x_test, y_test))

# print("Features Importances:", print(rf.feature_importances_))
# print("Score out-of-bag:", rf.oob_score_)
# print("Probabilidades de classes para X_teste:", rf.predict_proba(x_test))

#normalizar os meus atributos: Pegar o maior valor de pixel e dividir todos pixeis por ele. 
