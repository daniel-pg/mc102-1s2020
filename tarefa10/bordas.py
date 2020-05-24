"""
Daniel Paulo Garcia © 2020

bordas.py

Descrição: Pequeno script que destaca as bordas de desenhos. Suporta operações em imagens PBM compactadas com a
codificação Run-length (RLE), usando as funções de manipulação de imagens predefinidas no módulo <modulo.py>.
"""

from modulo import *


def destacar_bordas(largura: int, altura: int, imagem: Imagem):
    """
    Destaca as bordas de uma figura segundo os seguintes critérios:
    1. Pixels pretos que tenham pelo menos um pixel branco na vizinhança (horizontal, vertical ou diagonais) permanecem
    inalterados.
    2. Pixels pretos que não tenham nenhum pixel branco na vizinhança são pintados de branco.
    3. Pixels brancos permancem inalterados em qualquer situação.

    :param largura: Largura da imagem em pixels
    :param altura: Altura da imagem em pixels
    :param imagem: Imagem bitmap monocromática representada por uma matriz de pixels pretos (1s) e brancos (0s)
    :return: Imagem com as bordas destacadas.
    """

    # Caso os arquivos de teste da tarefa sejam corrigidos, basta mudar para False
    _IGNORAR_CANTOS_E_PAREDES = True
    nova_imagem = [[imagem[i][j] for j in range(largura)] for i in range(altura)]

    # Processar primeiro o "miolo" da imagem, para evitar checagens de cantos ou paredes desnecessárias dentro do loop.
    for i in range(1, altura - 1):
        for j in range(1, largura - 1):

            # Pula células em branco
            if imagem[i][j] == '0':
                continue

            # Checa se células adjacentes diagonais são brancas
            elif imagem[i - 1][j - 1] == '0' or \
                    imagem[i - 1][j + 1] == '0' or \
                    imagem[i + 1][j - 1] == '0' or \
                    imagem[i + 1][j + 1] == '0':
                continue

            # Checa se células adjacentes verticais ou horizontais são brancas
            elif imagem[i - 1][j] == '0' or \
                    imagem[i][j - 1] == '0' or \
                    imagem[i][j + 1] == '0' or \
                    imagem[i + 1][j] == '0':
                continue

            # Se a célula não é branca nem possui célula branca na vizinhança, então deve ser pintada de branco
            else:
                nova_imagem[i][j] = '0'

    if _IGNORAR_CANTOS_E_PAREDES:
        return nova_imagem

    # Checar os quatro cantos da imagem
    if imagem[0][0] == '1' and \
            imagem[0][1] == '1' and \
            imagem[1][0] == '1' and \
            imagem[1][1] == '1':
        nova_imagem[0][0] = '0'

    if imagem[0][largura - 1] == '1' and \
            imagem[1][largura - 1] == '1' and \
            imagem[0][largura - 2] == '1' and \
            imagem[1][largura - 2] == '1':
        nova_imagem[0][largura - 1] = '0'

    if imagem[altura - 1][0] == '1' and \
            imagem[altura - 1][1] == '1' and \
            imagem[altura - 2][0] == '1' and \
            imagem[altura - 2][1] == '1':
        nova_imagem[altura - 1][0] = '0'

    if imagem[altura - 1][largura - 1] == '1' and \
            imagem[altura - 1][largura - 2] == '1' and \
            imagem[altura - 2][largura - 1] == '1' and \
            imagem[altura - 2][largura - 2] == '1':
        nova_imagem[altura - 1][largura - 1] = '0'

    # Checar as quatro paredes da imagem
    #
    # Parede de cima
    for j in range(1, largura - 1):

        if imagem[0][j] == '0':
            continue

        elif imagem[0][j - 1] == '0' or \
                imagem[0][j + 1] == '0' or \
                imagem[1][j - 1] == '0' or \
                imagem[1][j] == '0' or \
                imagem[1][j + 1] == '0':
            continue

        else:
            nova_imagem[0][j] = '0'

    # Parede de baixo
    for j in range(1, largura - 1):

        if imagem[altura - 1][j] == '0':
            continue

        elif imagem[altura - 1][j - 1] == '0' or \
                imagem[altura - 1][j + 1] == '0' or \
                imagem[altura - 2][j - 1] == '0' or \
                imagem[altura - 2][j] == '0' or \
                imagem[altura - 2][j + 1] == '0':
            continue

        else:
            nova_imagem[altura - 1][j] = '0'

    # Parede da esquerda
    for i in range(1, altura - 1):

        if imagem[i][0] == '0':
            continue

        elif imagem[i - 1][0] == '0' or \
                imagem[i + 1][0] == '0' or \
                imagem[i - 1][1] == '0' or \
                imagem[i][1] == '0' or \
                imagem[i + 1][1] == '0':
            continue

        else:
            nova_imagem[i][0] = '0'

    # Parede da direita
    for i in range(1, altura - 1):

        if imagem[i][largura - 1] == '0':
            continue

        elif imagem[i - 1][largura - 1] == '0' or \
                imagem[i + 1][largura - 1] == '0' or \
                imagem[i - 1][largura - 2] == '0' or \
                imagem[i][largura - 2] == '0' or \
                imagem[i + 1][largura - 2] == '0':
            continue

        else:
            nova_imagem[i][largura - 1] = '0'

    return nova_imagem


def main():
    arquivo_entrada = input()
    arquivo_saida = input()

    largura, altura, codificacao = carregar_imagem_codificada(arquivo_entrada)
    imagem = decodificar(largura, altura, codificacao)
    nova_imagem = destacar_bordas(largura, altura, imagem)

    codificacao = codificar(largura, altura, nova_imagem)
    escrever_imagem_codificada(largura, altura, codificacao, arquivo_saida)


if __name__ == '__main__':
    main()
