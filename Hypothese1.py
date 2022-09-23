import numpy as np
import matplotlib.pyplot as plt

from utils import *

image = plt.imread("girafe.jpg")
image = rgb2gray(image)
outputPred = codeImagePred(image,matpred = [[0.33,0.33],[0.33,0.0]])
print(f'Le taux de compression pour l\'image quelconque est de (methode predictif): {outputPred}')

outputAri = codeAri(image)
print(f'Le taux de compression pour l\'image quelconque est de (methode arithmetique): {outputAri}')

