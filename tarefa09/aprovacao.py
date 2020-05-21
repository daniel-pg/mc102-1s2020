"""
Daniel Paulo Garcia © 2020

aprovacao.py

Descrição: Determina se um aluno foi aprovado ou reprovado de acordo com os critérios de avaliação da matéria de MC102.
"""


def ler_lista_notas() -> list:
    """
    Lê uma lista de tarefas com suas respectivas notas da entrada padrão, e devolve uma lista com as notas de cada
    tarefa.
    """

    lista_notas = input().split()
    nova_lista = []

    for i in range(1, len(lista_notas), 2):
        nova_lista.append(lista_notas[i])

    return nova_lista


def ler_lista_presenca() -> list:
    """
    Lê a lista de presença da entrada padrão, e devolve uma lista contendo valores booleanos, onde True corresponde
    a uma presença, e False corresponde a uma falta.
    """

    lista_presenca = []

    while True:
        try:
            entrada = input()

            if entrada == "faltou":
                lista_presenca.append(False)
            else:
                lista_presenca.append(True)

        except EOFError:
            break

    return lista_presenca


def verifica_aprovacao(lista_presenca: list, lista_notas: list) -> bool:
    """
    Recebe a lista de presença com valores True para presença e False para uma falta, e uma lista de notas de A a D de
    um aluno. Se o aluno cumprir com os critérios de aprovação, retorna o valor True. Caso contrário, retorna False.
    """

    numero_presencas = 0

    for presenca in lista_presenca:
        if presenca:
            numero_presencas += 1

    frequencia = numero_presencas / len(lista_presenca)

    if "D" in lista_notas or frequencia < 0.75:
        return False
    else:
        return True


def main():
    lista_notas = ler_lista_notas()
    lista_presenca = ler_lista_presenca()
    aprovado = verifica_aprovacao(lista_presenca, lista_notas)

    if aprovado:
        print("Aprovadx")
    else:
        print("Reprovadx")


if __name__ == '__main__':
    main()
