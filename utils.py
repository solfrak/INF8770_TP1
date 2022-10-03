import array
from math import floor
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d


def rgb2gray(rgb):
    return np.dot(rgb[:,:],[0.299, 0.587, 0.114])

hex2bin = dict('{:x} {:04b}'.format(x,x).split() for x in range(16))

def float_dec2bin(d):
    
    #Note: je ne suis pas sûr que cela fonctionne toujours... J'ai fait un nombre de tests limité.
    
    hx = float(d).hex() #Conversion float vers hex
    p = hx.index('p')
    #Conversion hex vers bin avec la table
    bn = ''.join(hex2bin.get(char, char) for char in hx[2:p])
    code = list(bn)
    indice = code.index('.') # position du séparateur des décimales
    puissance = int(hx[p+2:]) # Décalage
    if puissance >= indice:
        #On ajoute des zéros pour pouvoir décaler le séparateur des décimales.
        zerosdeplus = "0" * (puissance-indice+1)
        bn = zerosdeplus + bn
        code = list(bn)
        indice = code.index('.') # nouvelle position du séparateur des décimales

    
    #Décalage du séparateur décimal selon la puissance    
    for i in range(0,puissance):
        temp = code[indice-i-1];
        code[indice-i-1] = code[indice-i]
        code[indice-i] = temp
     
    
    #Enlève les zéros de trop et la partie avant le séparateur décimal
    
    ind = code.index('.')+1
    code = code[ind:]
    ind= code[::-1].index('1')
    code = code[:(len(code)-ind)]   
    codebinaire = ''.join(code)

    return codebinaire
    
def codeImagePred(image, matpred):

    col=image[:,0]
    image = np.column_stack((col,image))
    col=image[:,len(image[0])-1]
    image = np.column_stack((col,image))
    row=image[0,:]
    image = np.row_stack((row,image))
    row=image[len(image)-1,:]
    image = np.row_stack((row,image))

    

    erreur = np.zeros((len(image)-2,len(image[0])-2))
    imagepred = np.zeros((len(image)-2,len(image[0])-2))
    for i in range(1,len(image)-2):
        for j in range(1,len(image[0])-2):
            imagepred[i][j]=image[i-1][j-1]*matpred[0][0]+image[i-1][j]*matpred[0][1]+image[i][j-1]*matpred[1][0]
            erreur[i][j]=imagepred[i][j]-image[i][j]

    hist, intervalles = np.histogram(erreur, bins=100)
    
    counter = 0
    for i in hist:
        if i != 0:
            counter += 1
    print(f'Le nombre de valeur differente est de: {counter}')
    return 1 - (counter / 256)

def codeAri(input, isImage):
    Message = input
    if isImage:
        Message = array.array('f', input.flatten())
    
    ProbSymb =[[Message[0], Message.count(Message[0])/len(Message)]]
    nbsymboles = 1

    for i in range(1,len(Message)):
        if not list(filter(lambda x: x[0] == Message[i], ProbSymb)):
            ProbSymb += [[Message[i], ProbSymb[-1][1]+Message.count(Message[i])/len(Message)]]
            nbsymboles += 1
    longueurOriginale = len(input)
    if isImage:
        longueurOriginale = np.ceil(np.log2(nbsymboles))*len(Message)

    Code = ProbSymb[:]
    Code = [['', 0]] + ProbSymb[:]
    for i in range(len(Message)): 
        #Cherche dans quel intervalle est le symbole à coder
        temp = list(filter(lambda x: x[0] == Message[i], Code))
        indice = Code.index(temp[0])

        #Calcul des bornes pour coder le caractère
        Debut = Code[indice-1][1]
        Plage = Code[indice][1] - Debut
        Code = [['', Debut]]  
        for j in range(len(ProbSymb)):
            Code += [[ProbSymb[j][0], Debut+ProbSymb[j][1]*Plage]]
          
        ok = True
        valfinale = 0
        valEnBits = list('')
        p = 0
        while ok:
            p += 1
            #Essayer différentes sommes de puissance négative de 2
            valfinale += np.power(2.0,-p)
            valEnBits += '1' 
            if valfinale >= (Debut + Plage):
                valfinale -= np.power(2.0,-p) #Hors de la borne maximale, on annule l'ajout.
                valEnBits[-1] ='0'
            elif valfinale >= Debut :
                ok = False

        messagecode = float_dec2bin(valfinale) #Essayer d'autres valeurs qui tombent dans l'intervalle
        print(f'La longueur du message encode est de: {len(messagecode)} et la longueur du message original est de : {longueurOriginale}')
        return 1 - (len(messagecode) / longueurOriginale)
        # return valfinale, ProbSymb, longueurOriginale


def codagePred1D(input):

    erreur = np.zeros(len(input))
    erreur[0] = floor(input[0])
    for i in range(1, len(input)):
        code = input[i]
        erreur[i] = code - floor(input[i-1])

    hist, intervalles = np.histogram(erreur, bins=100)
        
    counter = 0
    for i in hist:
        if i != 0:
            counter += 1
    print(f'Le nombre de valeur differente est de: {counter}')
    return 1 - (counter / (max(input) - min(input) + 1))
    # return erreur

def decodageSonPred(arrayErreur):
    decode = np.zeros(len(arrayErreur))
    decode[0] = arrayErreur[0]
    for i in range(1,len(arrayErreur)):
        erreur = arrayErreur[i]
        decode[i] = decode[i - 1] + erreur
    print(decode)


def decodageSonAri(val, prob, length):
    msg_decode = []
    while len(msg_decode) < length:
        # search for the index
        idx = 0
        while val >= prob[idx][1]:
            idx += 1
        
        #get the symbol
        carac = prob[idx][0]
        msg_decode.append(carac)

        #update the value
        if idx == 0:
            val /= prob[idx][1]
        else:
            val = (val - prob[idx-1][1])/(prob[idx][1]-prob[idx-1][1])
    
    return(msg_decode)


def customCount(list, valeur):
    compteur = 0
    for i in list:
        if i == valeur:
            compteur += 1
    return compteur
def calculateProb(message):
   
    myDict = {}
    for i in range(0, len(message)):
        if not myDict.get(message[i]):
            myDict.update({message[i] : customCount(message, message[i]) / len(message)})
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
        if min == max:
            valfinale = min
            break
        #Essayer différentes sommes de puissance négative de 2
        valfinale += np.power(2.0,-p)
        valEnBits += '1' 
        if valfinale >= (min + (max - min)):
            valfinale -= np.power(2.0,-p) #Hors de la borne maximale, on annule l'ajout.
            valEnBits[-1] ='0'
        elif valfinale >= min :
            ok = False
    messagecode = float_dec2bin(valfinale)
    longueurOriginale = len(input)
    print(f'La longueur du message encode est de: {len(messagecode)} et la longueur du message original est de : {longueurOriginale}')

    return valfinale










