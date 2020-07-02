"""
Daniel Paulo Garcia © 2020

agenda.py

Descrição: ???
"""

import argparse
import csv
import typing


def inicializar_agenda(nome_arquivo: str):
    """Cria uma nova agenda vazia e guarda em um arquivo no caminho especificado."""
    with open(nome_arquivo, mode='w', encoding="UTF-8") as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=',')
        csv_writer.writerow(["nome", "descrição", "data", "hora"])


def criar_evento(nome_arquivo: str, nome_evnt: str, data_evnt: str, hora_evnt: str, descricao_evnt: str):
    """docstring"""
    pass


def alterar_evento(nome_arquivo: str, evento: int, nome_evnt: str, data_evnt: str, hora_evnt: str, descricao_evnt: str):
    """docstring"""
    pass


def remover_evento(nome_arquivo: str, evento: int):
    """docstring"""
    print(evento)


def listar_eventos(nome_arquivo: str, data_evnt: str):
    """docstring"""
    pass


def processar_argumentos():
    """docstring"""
    parser = argparse.ArgumentParser(description="(inserir nome cafona aqui)! O melhor aplicativo de agenda para linha"
                                                 "de comando que você jamais verá!")
    parser.add_argument("-a", "--agenda", required=True, help="Especifica o caminho do arquivo CSV da agenda.")

    subparsers = parser.add_subparsers(title="Ação", dest="action",
                                       help="Especifica uma ação a ser executada pelo programa")

    # Comandos do programa
    parser_inicializar = subparsers.add_parser("inicializar", help="Inicializar uma nova agenda vazia.")
    parser_criar = subparsers.add_parser("criar", help="Criar um novo evento na agenda.")
    parser_alterar = subparsers.add_parser("alterar", help="Altera os dados de um evento da agenda.")
    parser_remover = subparsers.add_parser("remover", help="Remove um evento da agenda.")
    parser_listar = subparsers.add_parser("listar", help="Listar eventos da agenda.")

    # Argumentos em comum para alguns dos comandos
    for cmd in [parser_inicializar, parser_criar, parser_alterar]:
        cmd.add_argument("--nome", help="")
        cmd.add_argument("--data", help="")
        cmd.add_argument("--hora", help="")
        cmd.add_argument("--descricao", help="")

    parser_alterar.add_argument("--evento", help="")
    parser_remover.add_argument("--evento", help="")
    parser_listar.add_argument("--data", help="")

    return parser.parse_args()


def main():
    args = processar_argumentos()

    operacoes = {
        "inicializar": lambda agenda: inicializar_agenda(agenda),
        "criar": lambda agenda: criar_evento(agenda, args.nome, args.data, args.hora, args.descricao),
        "alterar": lambda agenda: alterar_evento(agenda, args.evento, args.nome, args.data, args.hora, args.descricao),
        "remover": lambda agenda: remover_evento(agenda, args.evento),
        "listar": lambda agenda: listar_eventos(agenda, args.data),
    }

    operacao_selecionada = operacoes.get(args.action)
    operacao_selecionada(args.agenda)


if __name__ == '__main__':
    main()
