"""
Daniel Paulo Garcia © 2020

frequencia.py

Descrição: ???
"""

from typing import List, Tuple

ListaDePalavras = List[str]


def calcular_quartis():
    """docstring"""
    pass


def separar_palavras(texto: str, stop_words: ListaDePalavras):
    """docstring"""
    lista_palavras = []
    palavra = ""

    for c in range(len(texto)):

        if texto[c] == ' ' or texto[c] == ',':
            if palavra not in stop_words:
                lista_palavras.append(palavra)
            palavra = ""
            continue

        palavra += texto[c]

    return lista_palavras


def ler_entrada() -> ListaDePalavras:
    """
    Lê duas linhas da entrada padrão, a primeira contendo o caminho do arquivo de texto a ser processado e a segunda
    contendo as stop words (palavras ignoradas pelo programa). Retorna a lista de palavras do texto ordenadas em ordem
    alfabetica invertida.

    ATUALIZAR DOCSTRING!
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

    # Imprimir as três palavras mais frequentes, da mais à menos frequente
    print(palavras[:2])

    # Imprimir número de palavras cuja frequência é maior ou igual à da última palavra do primeiro quartil, quando
    # consideramos as palavra da mais à menos frequente. Para determinar o quartil, desconsidere palavras que se repetem
    # menos de 5 vezes.

    # Imprimir três palavras mais frequentes entre aquelas que não foram incluídas na contagem da linha anterior.

    # Quando necessário, use a ordem lexicográfica das palavras para resolver empates.


if __name__ == '__main__':
    main()
