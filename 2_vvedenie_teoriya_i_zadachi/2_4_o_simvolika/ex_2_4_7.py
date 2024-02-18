#Тест: правила работы с логарифмами
from math import log

n = 7

print('=============')
print(n**log(7,3)==7**log(n,3))
print(2**log(n,2) == n)
print(n**log(n,2) == n)
print(log((n**2),10) == 2*log(n,10))
