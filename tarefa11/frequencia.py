"""
Daniel Paulo Garcia © 2020

frequencia.py

Descrição: Conta a frequência com que as palavras aparecem em um arquivo de texto, para descobrir algumas
palavras-chaves.
"""

from modulo2 import DictPalavrasFrequencias
from modulo2 import calcular_quartis, ordenar_por_frequencia, contar_palavras


def ler_entrada() -> DictPalavrasFrequencias:
    """
    Lê duas linhas de texto da entrada padrão, a primeira contendo o caminho de um arquivo e a segunda uma lista
    separada de stop-words. Devolve uma lista com todas as palavras do texto, exceto as stop-words.
    """

    # Lê texto do arquivo especificado
    caminho_arquivo = input()
    arquivo_texto = open(caminho_arquivo, mode='r')
    texto = arquivo_texto.read()
    arquivo_texto.close()

    # Lê stop-words da entrada padrão
    stop_words = set(input().split())

    lista_palavras = contar_palavras(texto, stop_words)

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
    lista2 = list(filter(lambda x: x[1] > 5, lista_freq))
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
