"""
Daniel Paulo Garcia © 2020

probabilidade.py

Descrição: Recebe uma lista de números naturais separados por espaço e devolve outra lista onde os elementos aparecem
apenas uma vez. Os elementos da nova lista são sorteados por ordem crescente de frequência em que aparecem na entrada.
"""


def ordenar_lista(lista: list) -> list:
    """Ordena os elementos de uma lista de números em ordem crescente"""
    for _ in range(len(lista) - 1):
        # Previne que o algoritmo seja executado até o final caso a lista já esteja ordenada
        esta_ordenada = True

        for i in range(len(lista) - 1):
            if lista[i] > lista[i + 1]:
                lista[i], lista[i + 1] = lista[i + 1], lista[i]
                esta_ordenada = False

        if esta_ordenada:
            break

    return lista


def eliminar_elementos_repetidos(lista: list) -> list:
    """Remove elementos repetidos de maneira a manter a ordem em que aparecem na lista original"""
    k = 0
    nova_lista = []

    while k < len(lista):
        if lista[k] not in lista[:k]:
            nova_lista.append(lista[k])
        k += 1

    return nova_lista


def contar_frequencias(lista_elementos: list, lista_repetida: list) -> list:
    """Devolve uma lista cujo n-ésimo elemento corresponde ao número de ocorrências do n-ésimo elemento de
    lista_elementos na lista_repetida."""

    lista_frequencias = []

    for a in lista_elementos:
        frenquencia = 0
        for b in lista_repetida:
            if a == b:
                frenquencia += 1
        lista_frequencias.append(frenquencia)

    return lista_frequencias


def ordenar_por_frequencia(lista_elementos: list, lista_frequencias: list) -> list:
    """Ordena os elementos de lista_elementos em ordem crescente das suas frequências."""

    if len(lista_elementos) != len(lista_frequencias):
        pass

    for _ in range(len(lista_elementos) - 1):
        # Previne que o algoritmo seja executado até o final caso a lista já esteja ordenada
        esta_ordenada = True

        for i in range(len(lista_elementos) - 1):
            if lista_frequencias[i] > lista_frequencias[i + 1]:
                lista_frequencias[i], lista_frequencias[i + 1] = lista_frequencias[i + 1], lista_frequencias[i]
                lista_elementos[i], lista_elementos[i + 1] = lista_elementos[i + 1], lista_elementos[i]
                esta_ordenada = False

        if esta_ordenada:
            break

    return lista_elementos


def main():
    entrada = input().split()

    # Converte os elementos da entrada de string para int
    for i in range(len(entrada)):
        entrada[i] = int(entrada[i])

    lista_sem_repetidos = eliminar_elementos_repetidos(entrada)

    # No caso de dois números diferentes terem a mesma probabilidade, o menor elemento deve vir antes.
    lista_sem_repetidos = ordenar_lista(lista_sem_repetidos)

    lista_frequencias = contar_frequencias(lista_sem_repetidos, entrada)
    lista_sem_repetidos = ordenar_por_frequencia(lista_sem_repetidos, lista_frequencias)

    # Imprime os elementos da lista separados por espaços
    for i in range(len(lista_sem_repetidos) - 1):
        print(lista_sem_repetidos[i], end=" ")

    print(lista_sem_repetidos[-1], end="")  # Último elemento não tem espaço


if __name__ == '__main__':
    main()
