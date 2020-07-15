"""
Daniel Paulo Garcia © 2020

mmc.py

Descrição: Dados dois números, a e b, calcula o mínimo múltiplo comum entre eles.
"""


def calcular_mdc(a, b):
    if b == 0:
        return a
    else:
        return calcular_mdc(b, a % b)


def calcular_mmc(a, b):
    return (a // calcular_mdc(a, b)) * b


def main():
    a, b = [int(n) for n in input().split()]
    resultado = calcular_mmc(a, b)
    print(resultado)


if __name__ == '__main__':
    main()
