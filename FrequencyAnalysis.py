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


new_line_count = 0

#
for c in freq: # 
    print(c, ':', freq[c],' ', end='') #parametr end na konec vypisu vklada mezere
    if new_line_count % 3 == 2: #pocitame od 0 pak 1 a pak 2 a hele zbytek 2 hodim tam enter
        print()
    new_line_count += 1

