from math import floor
import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
from utils import *

[fs, x] = wavfile.read('0125.wav')
print(x)
output1 = codagePred1D(x)
print(f'Le taux de compression avec la methode predictive est de: {output1}')

output2 = codeAri(x)
print(f'Le taux de compression avec la methode arithmetique est de: {output2}')
