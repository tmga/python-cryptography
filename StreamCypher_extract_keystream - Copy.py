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


def modification(cipher):
    mod = [0]*len(cipher)
    mod[10] = ord(' ') ^ ord('1')
    mod[11] = ord(' ') ^ ord('0')
    mod[12] = ord('1') ^ ord('0')
    return bytes([mod[i] ^ cipher[i] for i in range(len(cipher))])

def get_key(message, cipher):
    return bytes([message[i] ^ cipher[i] for i in range(len(cipher))])


def crack(key_stream, cipher):
    length = min(len(key_stream), len(cipher))
    return bytes([key_stream[i] ^ cipher[i] for i in range(length)])

#Eve goes to Alice
eves_message = "This is the most valued secrets of all her life.".encode()

#This is Alice alone
key = KeyStream(10)
message = eves_message
print(message)
cipher = encrypt(key, message)
print(cipher)

#This is Eve (alone) all evil
eves_key_stream = get_key(eves_message, cipher)


#This is Bob
key = KeyStream(10)
message = encrypt(key, cipher)
print(message)

#Alice again
message = "hi Bob, lets meet our world domination".encode()
key = KeyStream(10)
cipher = encrypt(key, message)
print(cipher)

#Bob again
key = KeyStream(10)
message = encrypt(key, cipher)
print(message)

#Eve again (more evil than ever)
print("This is EVE")
print(crack(eves_key_stream, cipher))