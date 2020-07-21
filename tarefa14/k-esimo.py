"""
Daniel Paulo Garcia © 2020

k-esimo.py

Descrição: Dada uma sequência de números não necessariamente ordenada e um número inteiro positivo k, encontra o k-ésimo
menor elemento.
"""


def particionar_sequencia(sequencia, inicio, fim):
    pivo = sequencia[(fim + inicio) // 2]
    i = inicio
    j = fim

    while True:
        while sequencia[i] < pivo:
            i += 1
        while sequencia[j] > pivo:
            j -= 1

        if i >= j:
            # O elemento na posição j já está ordenado
            return j

        sequencia[i], sequencia[j] = sequencia[j], sequencia[i]


def k_esimo(sequencia, inicio, fim, k):
    if inicio == fim:
        return sequencia[inicio]
    elif inicio < fim:
        p = particionar_sequencia(sequencia, inicio, fim)
        if k == p:
            return sequencia[k]
        elif k < p:
            return k_esimo(sequencia, inicio, p - 1, k)
        else:
            return k_esimo(sequencia, p + 1, fim, k)


def main():
    sequencia = [int(n) for n in input().split()]
    k = int(input()) - 1  # Infelizmente o k começa a contar do 1, e não do zero
    resultado = k_esimo(sequencia, 0, len(sequencia) - 1, k)
    print(resultado)


if __name__ == '__main__':
    main()
