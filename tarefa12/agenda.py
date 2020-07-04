"""
Daniel Paulo Garcia © 2020

agenda.py

Descrição: ???
"""

import argparse
import csv

# Constantes
CSV_DELIMITER = ','
HEADER = ["id", "nome", "data", "hora", "descricao"]
QUOTE_CHAR = '"'

csv.register_dialect("agenda_de_eventos", delimiter=CSV_DELIMITER, quotechar=QUOTE_CHAR)


def inicializar_agenda(nome_arquivo: str):
    """Cria uma nova agenda vazia e guarda em um arquivo no caminho especificado."""

    with open(nome_arquivo, mode='w', encoding="UTF-8", newline='') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=HEADER, dialect="agenda_de_eventos")
        csv_writer.writeheader()

    print(f"Uma agenda vazia '{nome_arquivo}' foi criada!\n")


def criar_evento(nome_arquivo: str, nome_evnt: str, data_evnt: str, hora_evnt: str, descricao_evnt: str):
    """Cria uma nova entrada na agenda, contendo seu identificador, nome, data, hora e descrição do evento. O número
    identificador do novo evento será o maior identificador armazenado na agenda mais um, exceto quando a agenda está
    vazia. Nesse caso o identificador começa a contar do número 1."""

    idx = 1

    with open(nome_arquivo, mode='r', encoding="UTF-8", newline='') as csv_file:
        csv_reader = csv.DictReader(csv_file, dialect="agenda_de_eventos")
        dados = list(csv_reader)

        if len(dados) > 0:
            linha_max = max(dados, key=lambda x: int(x.__getitem__(HEADER[0])))
            idx = int(linha_max.__getitem__(HEADER[0])) + 1

    with open(nome_arquivo, mode='a', encoding="UTF-8", newline='') as csv_file:
        csv_writer = csv.writer(csv_file, dialect="agenda_de_eventos")
        csv_writer.writerow([str(idx), nome_evnt, data_evnt, hora_evnt, descricao_evnt])

    print("Novo evento criado:\n")
    print("-----------------------------------------------")
    print(f"Evento {idx} - {nome_evnt}")
    print(f"Descrição: {descricao_evnt}")
    print(f"Data: {data_evnt}")
    print(f"Hora: {hora_evnt}")
    print("-----------------------------------------------")


def alterar_evento(nome_arquivo: str, evento: int, nome_evnt: str, data_evnt: str, hora_evnt: str, descricao_evnt: str):
    """Altera um evento dado o seu identificador, trocando seus valores antigos pelos novos fornecidos. Caso um novo
    valor não seja fornecido para um campo em específico, mantém o original."""

    with open(nome_arquivo, mode='r', encoding="UTF-8", newline='') as csv_file:
        csv_reader = csv.reader(csv_file.readlines(), dialect="agenda_de_eventos")

    with open(nome_arquivo, mode='w', encoding="UTF-8", newline='') as csv_file:
        csv_writer = csv.writer(csv_file, dialect="agenda_de_eventos")
        csv_writer.writerow(HEADER)

        next(csv_reader)
        for row in csv_reader:
            if int(row[0]) == evento:
                if nome_evnt is None:
                    nome_evnt = row[1]
                if data_evnt is None:
                    data_evnt = row[2]
                if hora_evnt is None:
                    hora_evnt = row[3]
                if descricao_evnt is None:
                    descricao_evnt = row[4]
                csv_writer.writerow([evento, nome_evnt, data_evnt, hora_evnt, descricao_evnt])
            else:
                csv_writer.writerow(row)


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
