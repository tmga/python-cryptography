import random

class KeyStream:
    def __init__(self, key=1):
        self.next = key

    def rand(self):
        self.next = (1103515245*self.next + 12345) % 2**31
        return self.next

    def get_key_byte(self):
        return self.rand() % 256

def encrypt(key, message):
    return bytes([message[i] ^ key.get_key_byte() for i in range(len(message))])


"""
def transmit(cipher, likely):
    b = []
    for c in cipher:
        if random.randrange(0, likely) == 0:
            c = c ^ random.randrange(0, 8)
        b.append(c)
    return bytes(b)
"""

def modification(cipher):
    mod = [0]*len(cipher)
    mod[10] = ord(' ') ^ ord('1')
    mod[11] = ord(' ') ^ ord('0')
    mod[12] = ord('1') ^ ord('0')
    return bytes([mod[i] ^ cipher[i] for i in range(len(cipher))])




#####################################################
#
#    ALICE ----10$----->Bank
#               ^
#               | zmeni to na 1000$
#    BOB---------
#
#
#####################################################

#This is Alice
key = KeyStream(10)
message = "Send Bob:   10$".encode()
print(message)
cipher = encrypt(key, message)
print(cipher)

#This is Bob
#cipher = transmit(cipher, 5)
cipher = modification(cipher)

#This is Alice
key = KeyStream(10)
message = encrypt(key, cipher)
print(message)


