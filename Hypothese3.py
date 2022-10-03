from math import floor
from random import sample
import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
from utils import *

[fs, x] = wavfile.read('0125.wav')
entre = x.tolist()
output1 = codagePred1D(x)
print(f'Le taux de compression avec la methode predictive est de: {output1}')

tauxCompressionsAri = codeAri(entre, False)

print(f'Le taux de compression avec la methode arithmetique est de: {tauxCompressionsAri}')
