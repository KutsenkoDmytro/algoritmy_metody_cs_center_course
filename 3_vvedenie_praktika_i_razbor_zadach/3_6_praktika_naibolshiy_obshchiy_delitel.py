import timing as t
from random import randint

def gcd(tp):
    '''Пользовательская функция.'''
    tp = list(tp)
    while tp[1] != 0:
        tp[0], tp[1] = tp[1], tp[0] % tp[1]
    return tp[0]


def gcd_it(ab: (int, int,)) -> int:
    assert ab[0] >= 0 and ab[1] >= 0
    while ab[0] != 0 and ab[1] != 0:
        ab = ab[1] % ab[0], ab[0]
    return max(ab)


def gcd_rec(ab: (int, int,)) -> int:
    assert ab[0] >= 0 and ab[1] >= 0
    if ab[0] == 0 or ab[1] == 0:
        return max(ab)
    return gcd_rec((ab[1] % ab[0], ab[0]))

base = randint(0,800)
t.compare([gcd,gcd_it, gcd_rec], [(randint(0,base),(randint(0,base))) for _ in range(100)])