"""
Daniel Paulo Garcia © 2020

modulo2.py

Descrição: Grupo de funções utilizadas pelos scripts frequencia.py e sugestao.py da tarefa 11.
"""

from typing import List, Tuple

ListaDePalavras = List[str]
PalavrasPorFrequencia = List[Tuple[str, int]]


def calcular_quartis(lista: PalavrasPorFrequencia) -> Tuple[int, int, int]:
    """Calcula os quartis de uma lista de palavras previamente organizada em ordem de frequência em que aparecem no
    texto, com desempate por ordem lexicográfica."""

    _N = len(lista)

    q1 = lista[round(0.25 * (_N - 3))][1]

    if _N % 2 == 0:
        if lista[_N // 2 - 1][0] < lista[_N // 2][0]:
            q2 = lista[_N // 2 - 1][1]
        else:
            q2 = lista[_N // 2][1]
    else:
        q2 = lista[round((_N - 1) // 2)][1]

    q3 = lista[round(0.75 * _N - 0.25)][1]

    return q1, q2, q3


def ordenar_por_frequencia(lista_palavras: ListaDePalavras) -> PalavrasPorFrequencia:
    """Ordena a lista de palavras em ordem decrescente de frequências. Usa a ordem lexicográfica para casos em que duas
    palavras aparecem com mesma frequência."""
    dicio_freq = dict()
    conjunto_elementos = set()

    for el in lista_palavras:
        if el not in conjunto_elementos:
            dicio_freq[el] = lista_palavras.count(el)
            conjunto_elementos.add(el)

    lista_freq = [(key, lista_palavras.count(key)) for key in dicio_freq.keys()]
    lista_freq.sort(key=lambda x: (-x[1], x[0]))

    return lista_freq


def separar_palavras(texto: str, stop_words: set = {}) -> ListaDePalavras:
    """Recebe uma string contendo texto em português e um conjunto de stop-words, e devolve uma outra lista com todas as
    palavras do texto, exceto as stop-words. Caso uma lista de stop-words não seja fornecida, usa uma lista vazia."""
    lista_palavras = []
    pontuacao = {' ', ',', '\n', '.', '!', '?', '\'', '\"', '(', ')', '[', ']'}
    palavra = ""

    for c in range(len(texto)):

        if texto[c] in pontuacao:
            palavra = palavra.lower()

            if palavra not in stop_words and palavra:
                lista_palavras.append(palavra)

            palavra = ""
            continue

        palavra += texto[c]

    return lista_palavras
