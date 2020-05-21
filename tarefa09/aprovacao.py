"""
Daniel Paulo Garcia © 2020

primos.py

Descrição: Determina se um aluno foi aprovado ou reprovado de acordo com os critérios de avaliação da matéria de MC102.
"""


def ler_lista_notas() -> list:
    """
    Lê uma lista de tarefas com suas respectivas notas da entrada padrão, e devolve uma lista com as notas de cada
    tarefa.
    """

    lista_notas = input().split()
    pular_elemento = True

    for nota in lista_notas:
        if pular_elemento:
            pular_elemento = False
            continue
        else:
            pular_elemento = True
            lista_notas.append(nota)

    return lista_notas


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


def main():
    lista_notas = ler_lista_notas()
    lista_presenca = ler_lista_presenca()

    numero_presencas = 0

    for presenca in lista_presenca:
        if presenca:
            numero_presencas += 1

    frequencia = numero_presencas / len(lista_presenca)

    if "D" in lista_notas or frequencia < 0.75:
        print("Reprovadx")
    else:
        print("Aprovadx")


if __name__ == '__main__':
    main()
