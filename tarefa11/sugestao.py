"""
Daniel Paulo Garcia © 2020

segestao.py

Descrição: Dados um arquivo de texto e uma lista de duplas de palavras, devolve uma sugestão de palavra pra cada dupla
baseada na frequência com que uma expressão aparece no texto.
"""

from modulo2 import ListaDePalavras
from modulo2 import separar_palavras


def sugerir_palavra(dupla, lista_palavras: ListaDePalavras) -> str:
    """
    Dados um texto e uma tupla contendo uma dupla de palavras, retorna uma sugestão de palavra que poderia vir depois
    dessa expressão baseado na frequência em que aparecem no texto.
    """
    dicio_frequencias = dict()

    # Note que não faz sentido checar pela próxima palavra após a dupla (penúltima, última)
    for i in range(0, len(lista_palavras) - 2):
        if lista_palavras[i] == dupla[0] and lista_palavras[i + 1] == dupla[1]:
            palavra = lista_palavras[i + 2]

            if palavra in dicio_frequencias:
                dicio_frequencias[palavra] += 1
            else:
                dicio_frequencias[palavra] = 1

    palavra_freq_max = max(dicio_frequencias, key=dicio_frequencias.__getitem__)
    freq_max = dicio_frequencias[palavra_freq_max]
    lista_freq_max = [k for k, v in dicio_frequencias.items() if v == freq_max]
    sugestao = min(lista_freq_max)
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
    lista_palavras = separar_palavras(texto)

    for dupla in duplas_palavras:
        sugestao = sugerir_palavra(dupla, lista_palavras)
        print(dupla[0] + " " + dupla[1] + " " + sugestao)


if __name__ == '__main__':
    main()
