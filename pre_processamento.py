import pandas as pd 
import cv2

#Setando o local e nome dos arquivos que serão utilizados
path = 'images/Nov_2015/'
files_name = [
    '20151111_merge_B1_cut.tif',
    '20151111_merge_B2_cut.tif',
    '20151111_merge_B3_cut.tif',
    '20151111_merge_B4_cut.tif',
    '20151111_merge_B5_cut.tif',
    '20151111_merge_B6_cut.tif',
    '20151111_merge_B7_cut.tif' 
]
path_target = 'images/earth_truth/'
file_target = '20151111_merge_B1_cut_raster.tif'

#Função que faz a leitura de uma imagem (Utilizando OpenCV)
def readImage(path):
    img = cv2.imread(path, cv2.IMREAD_UNCHANGED)
    return img

#Lista de exemplos e de imagens 
exemplos = list()
imagens = list()

#Realizo a leitura de cada imagem (bandas de 1 a 7) e armazeno-as na lista de imagens. 
for name in files_name:
    imagens.append(readImage(path + name))

y = readImage(path_target + file_target)

#Aqui realizo a filtragem dos dados baseado na imagem da verdade terrestre. 
for coord_x, line in enumerate(y):
    for coord_y, value in enumerate(line):
        if value == -99: #-99 Corresponde as regiões que não são amostras de classe. 
            continue
        exemplo = {}
        exemplo['x'] = coord_x
        exemplo['y'] = coord_y
        for banda, img in enumerate(imagens): #Então, para cada banda acesso a imagem na coordenada x, y (mesma coord que a verdade terrestre)
            exemplo[banda] = img[coord_x][coord_y]
        exemplo['classe'] = value
        exemplos.append(exemplo)

pd.DataFrame(exemplos).to_csv('dataset.csv', index = False)
pd.DataFrame(exemplos).to_json('dataset.json', index = False)
    


