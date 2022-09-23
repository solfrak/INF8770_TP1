import numpy as np
import matplotlib.pyplot as plt

from utils import *

image = plt.imread("girafe.jpg")
image = rgb2gray(image)
# outputPred = codeImagePred(image,matpred = [[0.33,0.33],[0.33,0.0]])
# print(f'Le taux de compression pour l\'image quelconque est de (methode predictif): {outputPred}')

print(image[0][0], image[0][1])
val_ari, prob_ari, len_ari = codeAri(image, True)
print(len_ari)
print(prob_ari)
print(val_ari)
#msg_decode_ari = decodageSonAri(val_ari,prob_ari,len_ari)

print(f'Le taux de compression pour l\'image quelconque est de (methode arithmetique): {outputAri}')

