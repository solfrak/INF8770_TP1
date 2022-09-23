from email import message
import random
import numpy as np
import matplotlib.pyplot as py
import array as arr
from utils import codagePred1D, codeAri



symboleMess1 = ['A', 'B', 'C']
symboleMess2 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

mess_len = 500
message1 = ""
message2 = ""

for i in range(mess_len):
    message1 += random.choice(symboleMess1)
    message2 += random.choice(symboleMess2)

message1_ASCII =np.zeros(mess_len)
message2_ASCII =np.zeros(mess_len)
for i, char in enumerate(message1):
    message1_ASCII[i] = ord(char)

for i, char in enumerate(message2):
    message2_ASCII[i] = ord(char)


message1_ouptut_pred = codagePred1D(message1_ASCII)
message1_ouptut_ari = codeAri(message1_ASCII)

print(message1_ouptut_pred)
print(message1_ouptut_ari)

message2_ouptut_pred = codagePred1D(message2_ASCII)
message2_ouptut_ari = codeAri(message2_ASCII)

print(message2_ouptut_pred)
print(message2_ouptut_ari)

