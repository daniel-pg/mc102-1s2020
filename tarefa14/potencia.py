"""
Daniel Paulo Garcia © 2020

potencia.py

Descrição: Dado dois números inteiros positivos a e b, calcula a ** b fazendo no máximo log2(b) chamadas recursivas.
"""


def potencia(a, b):
    if b == 0:
        return 1
    elif b == 1:
        return a
    elif b % 2 == 0:
        return potencia(a * a, b // 2)
    else:
        return a * potencia(a * a, (b - 1) // 2)


def main():
    a, b = [int(n) for n in input().split()]
    resultado = potencia(a, b)
    print(resultado)


if __name__ == '__main__':
    main()
