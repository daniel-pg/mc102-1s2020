"""
Daniel Paulo Garcia © 2020

modulo.py

Descrição: Módulo com funções especiais para processar imagens
"""

from typing import Tuple, List

Codificacao = List[int]
Imagem = List[List[int]]


def codificar(largura: int, altura: int, imagem: Imagem) -> str:
    """
    Converte uma matriz de valores booleanos (0s e 1s) em uma codificação run-length.

    :param largura: Largura da imagem em pixels
    :param altura: Altura da imagem em pixels
    :param imagem: Imagem bitmap monocromática representada por uma matriz de pixels pretos (1s) e brancos (0s)
    :return:
    """

    return codificacao


def decodificar(largura: int, altura: int, codificacao: Codificacao) -> Imagem:
    """
    Converte a codificação run-length da imagem PBM comprimida em uma matriz de valores booleanos (0s e 1s).

    :param largura: Largura da imagem em pixels
    :param altura: Altura da imagem em pixels
    :param codificacao:
    :return:
    """

    return imagem


def carregar_imagem_codificada(nome_do_arquivo: str) -> Tuple[int, int, Codificacao]:
    """
    Carrega uma imagem PBM comprimida com a codificação Run-length (RLE) do disco e lê seus conteúdos.

    :param nome_do_arquivo: Caminho do arquivo de imagem PBM comprimido.
    :return: Tupla contendo a largura, altura e seção de dados.
    """

    _MAGIC_NUMBER = "P1C"

    try:
        with open(nome_do_arquivo) as arquivo:
            assert arquivo.readline().strip() == _MAGIC_NUMBER

            largura, altura = arquivo.readline().split()
            largura, altura = int(largura), int(altura)

            codificacao = arquivo.readline().split()
            codificacao = [int(token) for token in codificacao]

    except AssertionError:
        print(f"AssertionError: Número mágico inválido. Valor esperado era {_MAGIC_NUMBER}.")
    except ValueError:
        print("ValueError: Dimensão da imagem inválida.")
    except OSError:
        print("OSError: Erro ao tentar abrir o arquivo.")

    return largura, altura, codificacao


def carregar_imagem_decodificada(nome_do_arquivo: str) -> Tuple[int, int, Imagem]:
    """
    Carrega uma imagem PBM descomprimida do disco e lê seus conteúdos.

    :param nome_do_arquivo: Caminho do arquivo de imagem PBM descomprimido.
    :return: Tupla contendo a largura, altura e seção de dados.
    """

    _MAGIC_NUMBER = "P1"
    imagem = []

    try:
        with open(nome_do_arquivo) as arquivo:
            assert arquivo.readline().strip() == _MAGIC_NUMBER

            largura, altura = arquivo.readline().split()
            largura, altura = int(largura), int(altura)

            for linha in arquivo:
                imagem.append(list(linha.strip()))

    except AssertionError:
        print(f"AssertionError: Número mágico inválido. Valor esperado era {_MAGIC_NUMBER}.")
    except ValueError:
        print("ValueError: Dimensão da imagem inválida.")
    except OSError:
        print("OSError: Erro ao tentar abrir o arquivo.")

    return largura, altura, imagem


def escrever_imagem_codificada(largura: int, altura: int, codificacao: str, nome_do_arquivo: str) -> None:
    """
    DOCSTRING

    :param largura: Largura da imagem em pixels
    :param altura: Altura da imagem em pixels
    :param codificacao:
    :param nome_do_arquivo: Caminho de onde o arquivo de imagem PBM comprimido deve ser salvo.
    :return:
    """
    pass


def escrever_imagem_decodificada(largura, altura, imagem, nome_do_arquivo) -> None:
    """
    DOCSTRING

    :param largura: Largura da imagem em pixels
    :param altura: Altura da imagem em pixels
    :param imagem: Imagem bitmap monocromática representada por uma matriz de pixels pretos (1s) e brancos (0s)
    :param nome_do_arquivo: Caminho de onde o arquivo de imagem PBM descomprimido deve ser salvo.
    :return:
    """
    pass
