"""
Daniel Paulo Garcia © 2020

agenda.py

Descrição: ???
"""

import argparse
import csv
import typing


def inicializar_agenda(nome_arquivo: str):
    """docstring"""
    with open(nome_arquivo, mode='w', encoding="UTF-8") as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=',')
        csv_writer.writerow(["nome", "descrição", "data", "hora"])


def criar_evento():
    """docstring"""
    pass


def alterar_evento():
    """docstring"""
    pass


def remover_evento():
    """docstring"""
    pass


def listar_eventos():
    """docstring"""
    pass


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("action", help="", type=str)
    parser.add_argument("-a", "--agenda", help="Especifica o caminho do arquivo de agenda", required=True, type=str)

    args = parser.parse_args()

    operacoes = {
        "inicializar": inicializar_agenda,
        "criar": criar_evento,
        "alterar": alterar_evento,
        "remover": remover_evento,
        "listar": listar_eventos,
    }

    operacoes[args.action](args.agenda)


if __name__ == '__main__':
    main()
