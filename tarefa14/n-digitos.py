"""
Daniel Paulo Garcia © 2020

n-digitos.py

Descrição: Dados dois números, n e s, encontra todas as combinações de n dígitos (0-9) cuja soma é o valor s, e imprime
todas combinações em ordem crescente.
"""


def encontrar_combinacoes(vetor, n, s):
    if s < 0:
        return

    elif s == 0:
        novo_vetor = vetor + tuple((0 for _ in range(n)))
        for c in novo_vetor:
            print(c, end="")
        print()
        return novo_vetor

    elif n == 1 and s <= 9:
        novo_vetor = vetor + (s,)
        for c in novo_vetor:
            print(c, end="")
        print()
        return novo_vetor

    else:
        for k in range(s + 1):
            novo_vetor = vetor + (k,)
            encontrar_combinacoes(novo_vetor, n - 1, s - k)


def main():
    n, s = [int(n) for n in input().split()]
    vetor = tuple()
    encontrar_combinacoes(vetor, n, s)


if __name__ == '__main__':
    main()
