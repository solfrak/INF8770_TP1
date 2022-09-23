from ctypes import util
from email import message
import utils
import numpy as np

# val = 0.17

# prob = np.array([[ord('W'),0.25],[ord('I'),0.75],[ord('K'),1]])
# length = 4

# msg_decode = utils.decodageSonAri(val, prob, length)
# print(msg_decode)

# message = np.zeros(4)

# message[0] = 87
# message[0] = 73
# message[0] = 75
# message[0] = 73

message = [87, 73, 75, 73]

val, prob, long = utils.codeAri(message, False)

print(utils.decodageSonAri(val, prob, long))