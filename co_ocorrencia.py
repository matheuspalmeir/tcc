import skimage 
import pandas as pd 
import cv2
import numpy as np
import mahotas as mt
from skimage import img_as_int, img_as_float
from skimage.feature import greycomatrix, greycoprops
from sklearn.preprocessing import normalize, minmax_scale

#Setando local das imagens que serão utilizadas para gerar a matriz de Co-Ocorrência 
path = 'images/Nov_2015/'
files_name = [
    '20151111_merge_B1_cut',
    '20151111_merge_B2_cut'
]

#Função que faz a leitura de uma imagem (Utilizando OpenCV)
def readImage(path):
    img = cv2.imread(path, cv2.IMREAD_UNCHANGED)
    return img

def extract_features(image):
    #Extraindo as características de textura (correlação, homogeneidade, variancia, media)
    textures = mt.features.haralick(image, ignore_zeros=True, return_mean= True, distance=3)
    #print("Texturas " + textures)
 
    # take the mean of it and return it
    ht_mean = textures.mean(axis=0)
    return ht_mean

#Realizando a leitura das imagens 
imagens = list()
for name in files_name:
    img = readImage(path + name)
    # norm_image = cv2.normalize(img, None, alpha= -1, beta= 1, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_32F)
    # norm_image = normalize(img, norm="l1")
    int_img = img_as_int(norm_image)
    imagens.append(int_img)
    print("Imagem " + name + " lida!\n")
    print('image dtype ',img.dtype)

#Verificando os dados da imagem carregada
c = 0
for row in imagens[0]:
    for cell in row:
        if c == 10000: break
        print(cell, end=' ')
        c = c + 1
        

#Verificando a quantidade de níveis de cinza diferentes na imagem 
# data = list()
# data_csv = list()
# image_1 = imagens[0]
# image_2 = imagens[1]
# print("Imagens convertidas para int")
# print('image 1 dtype ',image_1.dtype)
# print('image 2 dtype ',image_1.dtype)


#Gerando a GLMC para cada imagem. 
# glmc_image_1 = greycomatrix(image_1, [3], [0, np.pi/4, np.pi/2, 3*np.pi/4], symmetric=True, normed=True)
# glmc_image_2 = greycomatrix(image_2,[3], [0, np.pi/4, np.pi/2, 3*np.pi/4], symmetric=True, normed=True)

#Gerando as features de textura 
texture_1 = extract_features(image_1)
texture_2 = extract_features(image_2)
print("Texturas extraídas!")


# feature_correlation_1= greycoprops(glmc_image_1, 'correlation')
# feature_homogeneity_1 = greycoprops(glmc_image_1, 'homogeneity')
# feature_main_1 = 
# feature_variance_1





