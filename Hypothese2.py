import numpy as np
import matplotlib.pyplot as plt

from utils import *


girafe = plt.imread("girafe.jpg")
girafe = rgb2gray(girafe)
degrade = plt.imread("degrade_de_gris.jpg")
degrade = rgb2gray(degrade)
damier = plt.imread("damier.jpg")
damier = rgb2gray(damier)

mat_girafe = [[0.33,0.33],[0.33,0.0]]
mat_degrade = [[0.5,0.0],[0.5,0.0]]
mat_damier = [[0.1,0.0],[0.0,0.0]]

NAME = ['girafe', 'degrade', 'damier']
IMAGES = [girafe, degrade, damier]
MATRICES = [mat_girafe, mat_degrade, mat_damier]

for i in range(len(IMAGES)):
    for m in range(len(MATRICES)):
        im = IMAGES[i]
        mat = MATRICES[m]
        output_pred = codeImagePred(im, mat)

        print(f'PREDICTIF : Le taux de compression pour l\'image {NAME[i]} avec la matrice {NAME[m]} est de: {output_pred}')



