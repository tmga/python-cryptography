import cProfile
from itertools import permutations

my_list = [1, 2 , 3, 4, 5]
cnt = 0
list_of_permutations = permutations(my_list)

for permutations in list_of_permutations:
    cnt += 1

print(len(permutations), cnt)


def faculty(n):
    if n <= 1:
        return n
    else:
        return faculty(n-1)*n

for i in range(10):
    print(faculty(i))


def counter(n):
    cnt = 0
    for i in range(n):
        cnt += 1
    return cnt

cProfile.run("counter(faculty(11))") #zobrazi cas vypoctu