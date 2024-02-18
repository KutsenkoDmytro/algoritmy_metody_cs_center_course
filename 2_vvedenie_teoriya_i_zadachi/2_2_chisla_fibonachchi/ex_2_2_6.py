'''
Задача на программирование: небольшое число Фибоначчи


Дано целое число
1≤n≤40, необходимо вычислить n-е число Фибоначчи (напомним, что F0 =0,F1 =1 и Fn =Fn−1 +Fn−2 при n≥2).

Sample Input:

3
Sample Output:

2
'''



def fib(n):
    a, b = 1, 0

    for i in range(n+1):
        a, b = b, a + b
    return a

def main():
    n = int(input())
    print(fib(n))


if __name__ == "__main__":
    main()