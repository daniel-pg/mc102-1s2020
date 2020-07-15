"""
Daniel Paulo Garcia © 2020

fatorial.py

Descrição: Calcula o fatorial de um número inteiro n não-negativo.
"""


def multiplicar_sequencia(inicio, fim):
    _N = fim - inicio + 1

    if _N == 0:
        return 1

    elif _N == 1:
        return inicio

    # Caso desnecessário, mas reduz o número de recursões pela metade de maneira bem trivial.
    elif _N == 2:
        return inicio * fim

    else:
        metade1 = multiplicar_sequencia(inicio, inicio + _N // 2)
        metade2 = multiplicar_sequencia(inicio + _N // 2 + 1, fim)
        return metade1 * metade2


def main():
    n = int(input())
    resultado = multiplicar_sequencia(1, n)
    print(resultado)


if __name__ == '__main__':
    main()
