import operator
import sys

cipher = """lrvmnir bpr sumvbwvr jx bpr lmiwv yjeryrkbi jx qmbm wi
bpr xjvni mkd ymibrut jx irhx wi bpr riirkvr jx
ymbinlmtmipw utn qmumbr dj w ipmhh but bj rhnvwdmbr bpr
yjeryrkbi jx bpr qmbm mvvjudwko bj yt wkbrusurbmbwjk
lmird jk xjubt trmui jx ibndt
  wb wi kjb mk rmit bmiq bj rashmwk rmvp yjeryrkb mkd wbi
iwokwxwvmkvr mkd ijyr ynib urymwk nkrashmwkrd bj ower m
vjyshrbr rashmkmbwjk jkr cjnhd pmer bj lr fnmhwxwrd mkd
wkiswurd bj invp mk rabrkb bpmb pr vjnhd urmvp bpr ibmbr
jx rkhwopbrkrd ywkd vmsmlhr jx urvjokwgwko ijnkdhrii
ijnkd mkd ipmsrhrii ipmsr w dj kjb drry ytirhx bpr xwkmh
mnbpjuwbt lnb yt rasruwrkvr cwbp qmbm pmi hrxb kj djnlb
bpmb bpr xjhhjcwko wi bpr sujsru msshwvmbwjk mkd
wkbrusurbmbwjk w jxxru yt bprjuwri wk bpr pjsr bpmb bpr
riirkvr jx jqwkmcmk qmumbr cwhh urymwk wkbmvb"""

#######################################################################################################################################
""" 
alphabet = "abcdefghijklmnopqrstuvwxyz"
freq = {} #slovnik
letter_count = 0

for c in alphabet: #kazdemu pismenu v abecede priradi nulu 
    freq[c] = 0 #vytvori list
    #freq[a] = 0
    #freq[b] = 0
    #.
    #.
    #.

for c in cipher: #pro vsechny znaky v sifre 
    if c in freq: #jestli je ve freq priradi jedna
        freq[c] += 1 #projizdi se retezec bere se kazde pismenko a inkrementuje se mu hodnota o 1
        letter_count += 1

for c in freq:
    freq[c] = round(freq[c]/letter_count,4) #pocita se vyskyt v procente a zaokrouhluje se hodnota na 4 desetina mista


for c in freq: 
    print(c, ':', freq[c],' ', end='') #parametr end na konec vypisu vklada mezere
    if new_line_count % 3 == 2: #pocitame od 0 pak 1 a pak 2 a hele zbytek 2 hodim tam enter
        print()
    new_line_count += 1

"""
class Attack:
    def __init__(self):
        self.alphabet = "abcdefghijklmnopqrstuvwxyz"
        self.plain_chars_left = "abcdefghijklmnopqrstuvwxyz"
        self.cipher_chars_left = "abcdefghijklmnopqrstuvwxyz"
        self.freq = {}
        self.freq_eng = {'a': 0.0817, 'b': 0.0150, 'c': 0.0278, 'd': 0.0425, 'e': 0.1270, 
        'f': 0.0223, 'g': 0.0202, 'h': 0.0609, 'i': 0.0697, 'j': 0.0015, 'k': 0.0077,
         'l': 0.0403, 'm': 0.0241, 'n': 0.0675, 'o': 0.0751, 'p': 0.0193, 'q': 0.0010, 
         'r': 0.0599, 's': 0.0633, 't': 0.0906, 'u': 0.0276, 'v': 0.0098, 'w': 0.0236,
          'x': 0.0015, 'y': 0.0197, 'z': 0.0007}
        self.mappings = {}



    def calculate_freq(self, cipher):
        for c in self.alphabet: #kazdemu pismenu v abecede priradi nulu 
            self.freq[c] = 0 #vytvori list
        
        letter_count = 0
        
        for c in cipher: #pro vsechny znaky v sifre 
            if c in self.freq: #jestli je ve freq priradi jedna
                self.freq[c] += 1 #projizdi se retezec bere se kazde pismenko a inkrementuje se mu hodnota o 1
                letter_count += 1

        for c in self.freq:
            self.freq[c] = round(self.freq[c]/letter_count,4) #pocita se vyskyt v procente a zaokrouhluje se hodnota na 4 desetina mista

    def print_freq(self):
        new_line_count = 0
        for c in self.freq: 
            print(c, ':', self.freq[c],' ', end='') #parametr end na konec vypisu vklada mezere
            if new_line_count % 3 == 2: #pocitame od 0 pak 1 a pak 2 a hele zbytek 2 hodim tam enter
                print()
            new_line_count += 1

    def calculate_matches(self):
        for cipher_char in self.alphabet:  
            map = {}
            for plain_char in self.alphabet: #pro kazdy znak v abecede
                map[plain_char] = round(abs(self.freq[cipher_char] - self.freq_eng[plain_char]), 4) #ulozim do slovniku a odectu pravdepodovnosti pro kazde pismeno
            self.mappings[cipher_char] = sorted(map.items(), key=operator.itemgetter(1)) #srovnam ho od nejmensi po nejvetsi, z modulu operator 

    def guess_key(self):
        key = {}
        for cipher_char in self.cipher_chars_left:
            for plain_char, diff in self.mappings[cipher_char]:
                if plain_char in self.plain_chars_left:
                    key[cipher_char] = plain_char
                    self.plain_chars_left = self.plain_chars_left.replace(plain_char, '')
                    break
        return key
        
def decrypt(key, cipher):
    message = ""
    for c in cipher:
        if c in key:
            message += key[c]
        else:
            message += c
    return message


attack = Attack()
attack.calculate_freq(cipher)
attack.print_freq()
attack.calculate_matches()
key=attack.guess_key()

print()
print(key)

message = decrypt(key, cipher)

print()
print(message)

"""
print()
for c in attack.mappings: #a vsechno vypisu
    print(c, attack.mappings[c])
"""