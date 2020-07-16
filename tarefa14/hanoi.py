"""
Daniel Paulo Garcia © 2020

hanoi.py

Descrição: Determina o número mínimo de movimentos para resolver o problema da torre de Hanói com n discos.
"""


def hanoi(n):
    if n == 1:
        return 1
    else:
        return 2 * hanoi(n - 1) + 1


def main():
    n = int(input())
    resultado = hanoi(n)
    print(resultado)


if __name__ == '__main__':
    main()
