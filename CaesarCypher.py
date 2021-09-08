def generate_key(n):
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    key = {} #dictionary
    cnt = 0
    for c in letters:
        key[c] = letters[(cnt + n) % len(letters)] #modulo pouzije kdyz se dostane na konec abecedy
        cnt += 1
    return key


def get_decryption_key(key):
    dkey = {}
    for c in key:
        dkey[key[c]] = c
    return dkey

def encrypt(key, message):
    cipher = ""
    for c in message:
        if c in key:
            cipher += key[c]
        else:
            cipher += c
    return cipher

#ENEMY
key = generate_key(3)
print(key)
message = "YOU ARE AWESOME"
cipher = encrypt(key,message)
#print(cipher)


#WE BREAKING CIPHER
#dkey = get_decryption_key(key)
#print(dkey)
#dkey = generate_key(26-3)
#message = encrypt(dkey, cipher)  
#print(message) 
for i in range(26):
    dkey = generate_key(i)
    message=encrypt(dkey,cipher)
    print(message)   