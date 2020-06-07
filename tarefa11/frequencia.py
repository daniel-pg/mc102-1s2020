from typing import List, Tuple

Texto = List[str]


def ler_entrada() -> Tuple[Texto, Texto]:
    """
    Lê duas linhas da entrada padrão, a primeira contendo o caminho do arquivo de texto a ser processado e a segunda
    contendo as stop words (palavras ignoradas pelo programa). Retorna a lista de palavras do texto ordenadas em ordem
    alfabetica invertida e a lista de stop words na ordem em que foram fornecidas.
    """
    caminho_arquivo = input()
    arquivo_texto = open(caminho_arquivo)
    texto = sorted(arquivo_texto.read().split())
    arquivo_texto.close()

    stop_words = input().split()
    return texto, stop_words


def main():
    texto, stop_words = ler_entrada()

    # Imprimir as três palavras mais frequentes, da mais à menos frequente

    # Imprimir número de palavras cuja frequência é maior ou igual à da última palavra do primeiro quartil, quando
    # consideramos as palavra da mais à menos frequente. Para determinar o quartil, desconsidere palavras que se repetem
    # menos de 5 vezes.

    # Imprimir três palavras mais frequentes entre aquelas que não foram incluídas na contagem da linha anterior.

    # Quando necessário, use a ordem lexicográfica das palavras para resolver empates.


if __name__ == '__main__':
    main()
