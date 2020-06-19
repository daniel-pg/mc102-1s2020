"""
Daniel Paulo Garcia © 2020

frequencia.py

Descrição: Conta a frequência com que as palavras aparecem em um arquivo de texto, para descobrir algumas
palavras-chaves.
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


def contar_freq_palavra(palavra: str, lista: ListaDePalavras) -> int:
    """Conta a frequência com que uma palavra aparece numa lista de palavras."""

    # Função desnecessária se pudesse usar o count() na tarefa...
    frequencia = 0

    for elemento in lista:
        if elemento == palavra:
            frequencia += 1

    return frequencia


def ordenar_por_frequencia(lista_palavras: ListaDePalavras) -> PalavrasPorFrequencia:
    """Ordena a lista de palavras em ordem decrescente de frequências. Usa a ordem lexicográfica para casos em que duas
    palavras aparecem com mesma frequência."""
    lista_sem_repetidos = eliminar_repetidos(lista_palavras)
    lista_freq = []

    for palavra in lista_sem_repetidos:
        novo_item = (palavra, contar_freq_palavra(palavra, lista_palavras))
        lista_freq.append(novo_item)

    for _ in range(len(lista_freq) - 1):
        # Previne que o algoritmo seja executado até o final caso a lista já esteja ordenada
        esta_ordenada = True

        for i in range(len(lista_freq) - 1):
            if lista_freq[i][1] < lista_freq[i + 1][1]:
                lista_freq[i], lista_freq[i + 1] = lista_freq[i + 1], lista_freq[i]
                esta_ordenada = False
            elif lista_freq[i][1] == lista_freq[i + 1][1]:
                if lista_freq[i][0] > lista_freq[i + 1][0]:
                    lista_freq[i], lista_freq[i + 1] = lista_freq[i + 1], lista_freq[i]
                    esta_ordenada = False

        if esta_ordenada:
            break

    return lista_freq


def eliminar_repetidos(lista: ListaDePalavras) -> ListaDePalavras:
    """Elimina todos os elementos repetidos de uma lista de palavras."""
    lista_sem_repetidos = []
    conjunto_elementos = set()

    for el in lista:
        if el not in conjunto_elementos:
            lista_sem_repetidos.append(el)
            conjunto_elementos.add(el)

    return lista_sem_repetidos


def separar_palavras(texto: str, stop_words: ListaDePalavras) -> ListaDePalavras:
    """Recebe uma string contendo texto em português e uma lista de stop-words, e devolve uma outra lista com todas as
    palavras do texto, exceto as stop-words."""
    lista_palavras = []
    pontuacao = (' ', ',', '\n', '.', '!', '?', '\'', '\"', '(', ')', '[', ']')
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


def ler_entrada() -> ListaDePalavras:
    """
    Lê duas linhas de texto da entrada padrão, a primeira contendo o caminho de um arquivo e a segunda uma lista
    separada de stop-words. Devolve uma lista com todas as palavras do texto, exceto as stop-words.
    """

    # Lê texto do arquivo especificado
    caminho_arquivo = input()
    arquivo_texto = open(caminho_arquivo)
    texto = arquivo_texto.read()
    arquivo_texto.close()

    # Lê stop-words da entrada padrão
    stop_words = input().split()

    lista_palavras = separar_palavras(texto, stop_words)

    return lista_palavras


def main():
    palavras = ler_entrada()

    # Existe maneira de fazer isso usando funções do Python, mas como não pode usar...
    lista_freq = ordenar_por_frequencia(palavras)

    # Imprimir as três palavras mais frequentes, da mais à menos frequente
    for i in range(2):
        print(lista_freq[i][0], end=' ')
    print(lista_freq[2][0])

    # Imprimir número de palavras distintas cuja frequência é maior ou igual à da palavra do primeiro quartil, quando
    # consideramos as palavra da mais à menos frequente. Para determinar o quartil, desconsidere palavras que se repetem
    # menos de 5 vezes ou exatamanente 5 vezes.
    lista2 = []

    for el in lista_freq:
        if el[1] > 5:
            lista2.append(el)

    q1, q2, q3 = calcular_quartis(lista2)

    contagem = 0
    for el in lista2:
        if el[1] >= q1:
            contagem += 1

    print(contagem)

    # Imprimir três palavras mais frequentes entre aquelas que não foram incluídas na contagem da linha anterior, exceto
    # as palavras que se repetem menos de 5 vezes ou exatamanente 5 vezes.
    lista3 = []

    for el in lista2:
        if el[1] < q1:
            lista3.append(el)

    print(lista3[0][0], lista3[1][0], lista3[2][0],)


if __name__ == '__main__':
    main()
