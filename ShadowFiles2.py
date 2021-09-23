import hashlib
import base64

def guess_password(salt, iterations, entropy):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for c1 in alphabet:
        for c2 in alphabet:
            password = str.encode(c1 + c2)
            value = base64.b64encode(hashlib.pbkdf2_hmac("sha512", password, salt, iterations, dklen=128))
            if value == entropy:
                return password
    return "".encode()
            

iterations = 1 #45454
salt = base64.b64decode("6VuJKkHVTdDelbNMPBxzw7INW2NkYlR/LoW4OL7kVAI=".encode())
validation = "SALTED-SHA512-PBKDF2"
entropy = "ZyqDZRfbupyspWuB2i+pv5A4+UiRtwDkQXIWs3OZVWLiUQDQJS59Xll3X1qGK125UEgLDGmh+LPbTwuyc6WQKsxBApds1aiWxDEbllAuJ6IHx0DVB96TztknTI5hA/9vgqECGYLbKFadTSfcWY/DTsxTtAgl2jtuzUJY3OM5q4s="

password = "??".encode()

password = guess_password(salt, iterations, entropy)
print(password)

value = base64.b64encode(hashlib.pbkdf2_hmac("sha512", password, salt, iterations, dklen=128))
print(value)
print(entropy)