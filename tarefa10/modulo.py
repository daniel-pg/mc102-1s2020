"""
Daniel Paulo Garcia © 2020

modulo.py

Descrição: Módulo com funções especiais para carregar, codificar/decodificar e gravar imagens PBM.
"""

from typing import Tuple, List

Codificacao = List[str]
Imagem = List[List[str]]


def codificar(largura: int, altura: int, imagem: Imagem) -> Codificacao:
    """
    Converte uma matriz de valores booleanos (0s e 1s) em uma codificação run-length.

    :param largura: Largura da imagem em pixels
    :param altura: Altura da imagem em pixels
    :param imagem: Imagem bitmap monocromática representada por uma matriz de pixels pretos (1s) e brancos (0s)
    :return: Lista de strings contendo a codificação run-length da imagem.
    """

    numero_repeticoes = 0
    token_repetido = (imagem[0][0], imagem[1][0])

    codificacao = []

    for i in range(0, altura, 2):
        for j in range(largura):
            if token_repetido == (imagem[i][j], imagem[i + 1][j]):
                numero_repeticoes += 1
            else:
                codificacao.append(str(numero_repeticoes))
                codificacao.append(token_repetido[0] + token_repetido[1])
                token_repetido = (imagem[i][j], imagem[i + 1][j])
                numero_repeticoes = 1

    codificacao.append(str(numero_repeticoes))
    codificacao.append(token_repetido[0] + token_repetido[1])

    return codificacao


def decodificar(largura: int, altura: int, codificacao: Codificacao) -> Imagem:
    """
    Converte a codificação run-length da imagem PBM comprimida em uma matriz de valores booleanos (0s e 1s).

    :param largura: Largura da imagem em pixels
    :param altura: Altura da imagem em pixels
    :param codificacao: Lista de strings contendo a codificação run-length da imagem.
    :return: Imagem bitmap monocromática representada por uma matriz de pixels pretos (1s) e brancos (0s)
    """

    # Inicializar matriz para valores nulos
    imagem = [['0' for _ in range(largura)] for _ in range(altura)]

    i, j = 0, 0

    for k in range(0, len(codificacao), 2):
        numero_repeticoes = int(codificacao[k])
        token_repetido = codificacao[k + 1]

        for q in range(numero_repeticoes):

            # 'Wrap-around' da linha
            if j == largura:
                j = 0
                i += 2

            imagem[i][j] = token_repetido[0]
            imagem[i + 1][j] = token_repetido[1]
            j += 1

    return imagem


def carregar_imagem_codificada(nome_do_arquivo: str) -> Tuple[int, int, Codificacao]:
    """
    Carrega uma imagem PBM comprimida com a codificação Run-length (RLE) do disco e lê seus conteúdos.

    :param nome_do_arquivo: Caminho do arquivo de imagem PBM comprimido.
    :return: Tupla contendo a largura, altura e seção de dados da imagem.
    """

    _MAGIC_NUMBER = "P1C"

    try:
        with open(nome_do_arquivo) as arquivo:
            assert arquivo.readline().strip() == _MAGIC_NUMBER

            largura, altura = arquivo.readline().split()
            largura, altura = int(largura), int(altura)

            codificacao = arquivo.readline().split()

    except AssertionError:
        print(f"AssertionError: Número mágico inválido. Valor esperado era {_MAGIC_NUMBER}.")
    except ValueError:
        print("ValueError: Dimensão da imagem inválida.")
    except OSError:
        print("OSError: Erro ao tentar abrir o arquivo.")

    return largura, altura, codificacao


def carregar_imagem_decodificada(nome_do_arquivo: str) -> Tuple[int, int, Imagem]:
    """
    Carrega uma imagem PBM decodificada do disco e lê seus conteúdos.

    :param nome_do_arquivo: Caminho do arquivo de imagem PBM descomprimido.
    :return: Tupla contendo a largura, altura e seção de dados da imagem.
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


def escrever_imagem_codificada(largura: int, altura: int, codificacao: Codificacao, nome_do_arquivo: str) -> None:
    """
    Grava uma imagem PBM comprimida com a codificação run-length em um arquivo do disco no caminho especificado.

    :param largura: Largura da imagem em pixels
    :param altura: Altura da imagem em pixels
    :param codificacao: Lista de strings contendo a codificação run-length da imagem.
    :param nome_do_arquivo: Caminho de onde o arquivo de imagem PBM comprimido deve ser salvo.
    :return:
    """

    _MAGIC_NUMBER = "P1C"

    try:
        with open(nome_do_arquivo, mode='a+') as arquivo:
            arquivo.write(_MAGIC_NUMBER + "\n")
            arquivo.write(str(largura) + " " + str(altura) + "\n")
            arquivo.write(' '.join(codificacao))

    except OSError:
        print("OSError: Erro ao tentar escrever para o arquivo.")


def escrever_imagem_decodificada(largura: int, altura: int, imagem: Imagem, nome_do_arquivo: str) -> None:
    """
    Grava uma imagem PBM decodificada em um arquivo do disco no caminho especificado.

    :param largura: Largura da imagem em pixels
    :param altura: Altura da imagem em pixels
    :param imagem: Imagem bitmap monocromática representada por uma matriz de pixels pretos (1s) e brancos (0s)
    :param nome_do_arquivo: Caminho de onde o arquivo de imagem PBM decodificado deve ser salvo.
    :return:
    """

    _MAGIC_NUMBER = "P1"

    try:
        with open(nome_do_arquivo, mode='a+') as arquivo:
            arquivo.write(_MAGIC_NUMBER + "\n")
            arquivo.write(str(largura) + " " + str(altura) + "\n")

            for i in range(altura - 1):
                linha = [str(celula) for celula in imagem[i]]
                arquivo.write(''.join(linha) + "\n")

            linha = [str(celula) for celula in imagem[altura - 1]]
            arquivo.write(''.join(linha))

    except OSError:
        print("OSError: Erro ao tentar escrever para o arquivo.")
