"""
Daniel Paulo Garcia © 2020

busca_binaria.py

Descrição: Dado um vetor de inteiros em ordem crescente e um número, retorna o índice da posição desse número no vetor,
ou então retorna -1 se esse número não está no vetor.
"""


def busca_binaria(vetor, i, inicio, fim):
    _N = fim - inicio + 1

    if _N == 1:
        if vetor[inicio] == i:
            return inicio
        else:
            return -1

    if _N == 2:
        if vetor[inicio] == i:
            return inicio
        elif vetor[fim] == i:
            return fim
        else:
            return -1

    else:
        metade1 = busca_binaria(vetor, i, inicio, inicio + _N // 2)
        if metade1 != -1:
            return metade1

        metade2 = busca_binaria(vetor, i, inicio + _N // 2 + 1, fim)
        if metade2 != -1:
            return metade2

        return -1


def main():
    vetor = [int(n) for n in input().split()]
    i = int(input())
    resultado = busca_binaria(vetor, i, 0, len(vetor) - 1)
    print(resultado)


if __name__ == '__main__':
    main()
