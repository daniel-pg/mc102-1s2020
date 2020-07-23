"""
Daniel Paulo Garcia © 2020

arvore.py

Descrição: Programa que recebe o link de uma página inicial e mostra a hierarquia entre as páginas que podem ser
alcançadas a partir da inicial.
"""

# Nunca é uma boa ideia importar usando *
from modulo import resolver_url, eh_url_valida, obter_html
import re


def imprimir_arvore(url: str, url_inicial: str, urls_ja_acessadas: set, espacos: int) -> None:
    """
    Dadas uma URL qualquer de um site e a URL de sua respectiva página principal, imprime recursivamente a árvore de
    todos os links acessíveis a partir da página, desde que estejam ou no mesmo diretório ou em subdiretórios da página
    inicial, e não sejam links externos.

    :param espacos:
    :param urls_ja_acessadas: Conjunto onde serão guardadas strings contendo as URL's que ja foram listadas pela função.
    :param url_inicial: URL da página inicial.
    :param url: URL a partir da qual será construída a árvore.
    :return:
    """

    if url in urls_ja_acessadas or not eh_url_valida(url, url_inicial):
        return
    else:
        html = obter_html(url)

        if html:
            url_pattern = re.compile(r'href=[\'"]([^#><@\s]+(?:\.html?|/))[\'"]')
            matches = re.finditer(url_pattern, html)
        else:
            return

        print((" " * espacos) + url)
        urls_ja_acessadas.add(url)

        for match in matches:
            url_encontrada = resolver_url(match.group(1), url_inicial)
            imprimir_arvore(url_encontrada, url, urls_ja_acessadas, espacos + 2)


def main():
    pagina_inicial = input()
    urls_ja_acessadas = set()
    imprimir_arvore(pagina_inicial, pagina_inicial, urls_ja_acessadas, 0)


if __name__ == '__main__':
    main()
