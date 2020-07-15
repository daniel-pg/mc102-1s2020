"""
Daniel Paulo Garcia © 2020

maximo.py

Descrição: Dada uma lista de elementos comparáveis, encontra o maior.
"""


def maximo(lista_numeros, inicio, fim):
    _N = fim - inicio + 1

    if _N == 1:
        return lista_numeros[inicio]

    # Caso desnecessário, mas reduz o número de recursões pela metade de maneira bem trivial.
    elif _N == 2:
        if lista_numeros[inicio] >= lista_numeros[fim]:
            return lista_numeros[inicio]
        else:
            return lista_numeros[fim]

    else:
        metade1 = maximo(lista_numeros, inicio, inicio + _N // 2)
        metade2 = maximo(lista_numeros, inicio + _N // 2 + 1, fim)
        if metade1 >= metade2:
            return metade1
        else:
            return metade2


def main():
    entrada = [int(n) for n in input().split()]
    valor_maximo = maximo(entrada, 0, len(entrada) - 1)
    print(valor_maximo)


if __name__ == '__main__':
    main()
