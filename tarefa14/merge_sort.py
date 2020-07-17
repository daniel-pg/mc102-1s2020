"""
Daniel Paulo Garcia © 2020

merge_sort.py

Descrição: Dada uma lista de elementos, ordena-a em ordem crescente usando do algoritmo de ordenação mergesort.
"""


def intercalar_sequencias(sequencia, inicio, divisor, fim):
    _N1 = divisor - inicio + 1
    _N2 = fim - divisor

    metade1, metade2 = [], []

    for i in range(_N1):
        metade1.append(sequencia[inicio + i])
    for j in range(_N2):
        metade2.append(sequencia[divisor + j + 1])

    metade1.append(float('inf'))
    metade2.append(float('inf'))

    i = 0
    j = 0

    for k in range(inicio, fim + 1):
        if metade1[i] <= metade2[j]:
            sequencia[k] = metade1[i]
            i += 1
        else:
            sequencia[k] = metade2[j]
            j += 1


def merge_sort(sequencia, inicio, fim):
    _N = fim - inicio + 1

    if _N == 2 and sequencia[inicio] > sequencia[fim]:
        sequencia[inicio], sequencia[fim] = sequencia[fim], sequencia[inicio]
    elif _N > 2:
        idx_metade = inicio + _N // 2
        merge_sort(sequencia, inicio, idx_metade)
        merge_sort(sequencia, idx_metade + 1, fim)
        intercalar_sequencias(sequencia, inicio, idx_metade, fim)


def main():
    sequencia = [int(n) for n in input().split()]
    merge_sort(sequencia, 0, len(sequencia) - 1)
    print(*sequencia)


if __name__ == '__main__':
    main()
