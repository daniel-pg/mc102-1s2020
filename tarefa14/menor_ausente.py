"""
Daniel Paulo Garcia © 2020

menor_ausente.py

Descrição: Dada uma sequência ordenada (crescente) de números, encontra o menor elemento ausente dessa sequência.
"""


def encontra_menor_ausente(sequencia, idx):
    if idx < len(sequencia) - 1:
        if sequencia[idx] == sequencia[idx + 1] - 1:
            return encontra_menor_ausente(sequencia, idx + 1)
        else:
            return sequencia[idx] + 1
    else:
        return -1


def main():
    entrada = [int(n) for n in input().split()]
    menor_ausente = encontra_menor_ausente(entrada, 0)
    print(menor_ausente)


if __name__ == '__main__':
    main()
