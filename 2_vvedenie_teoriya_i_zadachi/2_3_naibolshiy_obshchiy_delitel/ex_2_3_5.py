'''
Задача на программирование: наибольший общий делитель


По данным двум числам 1≤a,b≤2⋅10**9 найдите их наибольший общий делитель.

Sample Input 1:

18 35
Sample Output 1:

1
Sample Input 2:

14159572 63967072
Sample Output 2:

4
'''

def gcd(a, b):

    while b != 0:
        a, b = b, a % b
    return a


def main():
    a, b = map(int, input().split())
    print(gcd(a, b))


if __name__ == "__main__":
    main()