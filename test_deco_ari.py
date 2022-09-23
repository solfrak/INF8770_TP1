from email import message
from operator import index
from utils import *
import numpy as np
from scipy.interpolate import interp1d


def calculateProb(message):
   
    myDict = {}
    for i in range(0, len(message)):
        if not myDict.get(message[i]):
            myDict.update({message[i] : message.count(message[i]) / len(message)})
    for i, code in enumerate(myDict):
        if not i == 0:
            myDict[code] = myDict[code] + myDict[list(myDict)[i - 1]]
    return myDict


def codageAri1D(input):
    message = input
    dict = calculateProb(message)
    code = dict.copy()

    min = 0
    max = 1
    for i in message:
        max = code[i]
        if list(dict).index(i) >= 1:
            min = code[list(dict)[list(dict).index(i) - 1]]
        
        myMap = interp1d([0, 1], [min, max])
        for j in code:
            code[j] = float(myMap(dict[j]))
    print(f'My value should be beetween: {min} and {max}')

    ok = True
    valfinale = 0
    valEnBits = list('')
    p = 0
    while ok:
        p += 1
        #Essayer différentes sommes de puissance négative de 2
        valfinale += np.power(2.0,-p)
        valEnBits += '1' 
        if valfinale >= (min + (max - min)):
            valfinale -= np.power(2.0,-p) #Hors de la borne maximale, on annule l'ajout.
            valEnBits[-1] ='0'
        elif valfinale >= min :
            ok = False
    return valfinale


message = [87, 73, 75, 73]

# val, prob, long = utils.codeAri(message, False)
val = codageAri1D(message)
prob = np.array([[ord('W'),0.25],[ord('I'),0.75],[ord('K'),1]])
print(f'Ma valeur finale est: {val}')
print(f'Mon message decode est: {decodageSonAri(val, prob, 4)}')
