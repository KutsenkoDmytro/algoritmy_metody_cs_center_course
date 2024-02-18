def naive_ccd(a, b):
    for d in reversed(range(max(a,b)+1)):
        if d == 0 or a % d == b % d == 0:
            return d


print(naive_ccd(0,0))