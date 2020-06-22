"""
Daniel Paulo Garcia © 2020

segestao.py

Descrição: Dados um arquivo de texto e uma lista de duplas de palavras, devolve uma sugestão de palavra pra cada dupla
baseada na frequência com que uma expressão aparece no texto.
"""

from modulo2 import separar_palavras


def sugerir_palavra(dupla, texto):
    """
    Dados um texto e uma tupla contendo uma dupla de palavras, retorna uma sugestão de palavra que poderia vir depois
    dessa expressão baseado na frequência em que aparecem no texto.
    """
    frequencias = {}

    lista_palavras = separar_palavras(texto)

    # Note que não faz sentido checar pela próxima palavra após a dupla (penúltima, última)
    for i in range(0, len(lista_palavras) - 2):
        if lista_palavras[i] == dupla[0] and lista_palavras[i + 1] == dupla[1]:
            palavra = lista_palavras[i + 2]

            if palavra not in frequencias:
                frequencias[palavra] = 1
            else:
                frequencias[palavra] += 1

    freq_ordem_lexicografica = sorted(frequencias)
    sugestao = max(freq_ordem_lexicografica, key=lambda x: frequencias[x])
    return sugestao


def ler_entrada():
    """Lê um caminho de arquivo de texto e uma lista de duplas de palavras. Retorna o conteúdo do arquivo e a lista."""

    caminho_arquivo = input()
    arquivo = open(caminho_arquivo, mode='r')
    texto = arquivo.read()
    arquivo.close()

    duplas_palavras = []

    try:
        while True:
            dupla = tuple(input().split())
            duplas_palavras.append(dupla)

    except EOFError:
        return texto, duplas_palavras


def main():
    texto, duplas_palavras = ler_entrada()

    for dupla in duplas_palavras:
        sugestao = sugerir_palavra(dupla, texto)
        print(dupla[0] + " " + dupla[1] + " " + sugestao)


if __name__ == '__main__':
    main()
