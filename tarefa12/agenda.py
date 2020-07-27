"""
Daniel Paulo Garcia © 2020

agenda.py

Descrição: Uma pequena aplicação de linha de comando que permite gerenciar arquivos de agenda além de criar, alterar,
remover e listar eventos dessa agenda.
"""

from modulo_agenda import inicializar_agenda, criar_evento, alterar_evento, remover_evento, listar_eventos
import argparse


def processar_argumentos() -> argparse.Namespace:
    """
    Processa os argumentos do programa e retorna um objeto contendo os argumentos.

    :return: Objeto Namespace do argparse cujos atributos são os argumentos de linha de comando da aplicação.
    """

    parser = argparse.ArgumentParser(description="(inserir nome cafona aqui)! O melhor aplicativo de agenda para linha"
                                                 " de comando que você jamais verá!")
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
        cmd.add_argument("--nome", help="Nome do evento")
        cmd.add_argument("--data", help="Data do evento")
        cmd.add_argument("--hora", help="Horário do evento")
        cmd.add_argument("--descricao", help="Uma breve descrição do evento")

    parser_alterar.add_argument("--evento", type=int, help="")
    parser_remover.add_argument("--evento", type=int, help="")
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
