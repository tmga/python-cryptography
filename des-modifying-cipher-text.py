from pyDes import *

def modify(cipher):
    mod = [0]*len(cipher)
    #mod[10] = ord(' ') ^ ord('1')
    #mod[11] = ord(' ') ^ ord('0')
    #mod[12] = ord('1') ^ ord('0')
    mod[9] = 1
    return bytes([mod[i] ^ cipher[i] for i in range(len(cipher))])


message = "Give Bob:    10$ and send to him"
key = "DESCRYPT"
iv = bytes([0]*8)
k = des(key, CBC, iv, pad=None, padmode=PAD_PKCS5)

#Alice sending the encrypted message
cipher = k.encrypt(message)
print("Length of plain text:", len(message))
print("Length of cipher text:", len(cipher))
print("Encrypted:", cipher)

#Bob modifying the cipher text
cipher = modify(cipher)

#This is the bank decryption message
message = k.decrypt(cipher)
print("Decrypted:", message)
