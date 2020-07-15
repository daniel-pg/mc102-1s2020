"""
Daniel Paulo Garcia © 2020

fibonacci3.py

Descrição: Seja 3-Fibonacci uma variação da sequência de Fibonacci definida como f(n) = f(n-1) + f(n-2) + f(n-3), onde
f(n) = n se 0 <= n <= 2, calcula o n-ésimo número dessa sequência.
"""

memoria_fibonacci3 = {}


def fibonacci3(n):

    if n in memoria_fibonacci3:
        return memoria_fibonacci3[n]

    elif 0 <= n <= 2:
        return n

    else:
        resultado = fibonacci3(n-1) + fibonacci3(n-2) + fibonacci3(n-3)
        memoria_fibonacci3[n] = resultado
        return resultado


def main():
    n = int(input())
    resultado = fibonacci3(n)
    print(resultado)


if __name__ == '__main__':
    main()
