"""
Daniel Paulo Garcia © 2020

modulo2.py

Descrição: Grupo de funções utilizadas pelos scripts frequencia.py e sugestao.py da tarefa 11.
"""

# Import
from typing import List, Tuple, Dict

# Tipos de variáveis
ListaDePalavras = List[str]
DictPalavrasFrequencias = Dict[str, int]
PalavrasPorFrequencia = List[Tuple[str, int]]

# Constantes
_PONTUACAO = {' ', ',', '\n', '.', '!', '?', '\'', '\"', '(', ')', '[', ']'}


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


def ordenar_por_frequencia(dicio_freq: DictPalavrasFrequencias) -> PalavrasPorFrequencia:
    """
    Recebe um dicionário onde as chaves são palavras e os valores são frequências. Devolve uma lista de tuplas ordenada,
    onde cada tupla contém uma chave e um valor correspondente ao dicionário da entrada. A lista é organizada
    primeiramente em ordem decrescente de frequências, e depois pela ordem lexicográfica das palavras.
    """

    lista_freq = [(key, dicio_freq[key]) for key in dicio_freq.keys()]
    lista_freq.sort(key=lambda x: (-x[1], x[0]))

    return lista_freq


def separar_palavras(texto: str, stop_words: set = None) -> ListaDePalavras:
    """Recebe uma string contendo texto em português e um conjunto de stop-words, e devolve uma outra lista com todas as
    palavras do texto, exceto as stop-words. Caso uma lista de stop-words não seja fornecida, usa um conjunto vazio."""

    if stop_words is None:
        stop_words = {}

    lista_palavras = []
    palavra = ""

    for char in texto:

        if char in _PONTUACAO:
            palavra = palavra.lower()

            if palavra not in stop_words and palavra:
                lista_palavras.append(palavra)

            palavra = ""
            continue

        palavra += char

    return lista_palavras


def contar_palavras(texto: str, stop_words: set = None) -> DictPalavrasFrequencias:
    """
    Recebe uma string contendo texto em português e um conjunto de stop-words. Devolve um dicionário cujas chaves são
    todas as palavras do texto exceto as stop-words. Os valores de cada chave são suas respectivas frequências com que
    aparecem no texto. Caso uma lista de stop-words não seja fornecida, usa um conjunto vazio.
    """

    if stop_words is None:
        stop_words = {}

    dicio_freqs = dict()
    palavra = ""

    for char in texto:

        if char in _PONTUACAO:
            palavra = palavra.lower()

            if palavra not in stop_words and palavra:
                if palavra in dicio_freqs:
                    dicio_freqs[palavra] += 1
                else:
                    dicio_freqs[palavra] = 1

            palavra = ""
            continue

        palavra += char

    return dicio_freqs
