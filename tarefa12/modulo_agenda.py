"""
Daniel Paulo Garcia © 2020

modulo_agenda.py

Descrição: Módulo com as funções necessárias para manipular o arquivo de agenda.
"""

import csv
import logging
from typing import List, Dict

EventoAgenda = Dict[str, str]
Agenda = List[EventoAgenda]

# # Dialeto configurável do arquivo CSV da agenda
csv.register_dialect("agenda_de_eventos", delimiter=',', quotechar='"', skipinitialspace=True)

# Útil para diminuir a quantidade de mensagens exibidas no terminal durante os testes
root_logger = logging.getLogger()
logging.basicConfig(level=logging.WARN)


def inicializar_agenda(nome_arquivo: str) -> None:
    """
    Cria uma nova agenda vazia e guarda em um arquivo no caminho especificado.

    :param nome_arquivo: Caminho do arquivo CSV da agenda.
    :return:
    """

    agenda = []
    escrever_arquivo_agenda(nome_arquivo, agenda)
    root_logger.info(f"Uma agenda vazia '{nome_arquivo}' foi criada!\n")


def criar_evento(nome_arquivo: str, nome_evnt: str, data_evnt: str, hora_evnt: str, descricao_evnt: str) -> None:
    """
    Cria uma nova entrada na agenda, contendo seu identificador, nome, data, hora e descrição do evento. O número
    identificador do novo evento será o maior identificador armazenado na agenda mais um, exceto quando a agenda está
    vazia. Nesse caso o identificador começa a contar do número 1.

    :param nome_arquivo: Caminho do arquivo CSV da agenda.
    :param nome_evnt: Nome do evento.
    :param data_evnt: Data do evento.
    :param hora_evnt: Horário do evento.
    :param descricao_evnt: Descrição do evento.
    :return:
    """

    idx_novo_evnt = 1
    agenda = ler_arquivo_agenda(nome_arquivo)

    if len(agenda) > 0:
        linha_max = max(agenda, key=lambda x: int(x.__getitem__("id")))
        idx_novo_evnt = int(linha_max.__getitem__("id")) + 1

    novo_evnt = {"id": str(idx_novo_evnt),
                 "nome": nome_evnt,
                 "data": data_evnt,
                 "hora": hora_evnt,
                 "descricao": descricao_evnt}

    agenda.append(novo_evnt)
    escrever_arquivo_agenda(nome_arquivo, agenda)

    root_logger.info("Novo evento criado:\n")
    root_logger.info("-----------------------------------------------")
    imprimir_info_evnt(novo_evnt, modo_logger=True)


def alterar_evento(nome_arquivo: str, id_evento: int, nome_evnt: str, data_evnt: str, hora_evnt: str,
                   descricao_evnt: str) -> None:
    """
    Altera um evento dado o seu identificador, trocando seus valores antigos pelos novos fornecidos. Caso um novo
    valor não seja fornecido para um campo em específico, mantém o original.

    :param nome_arquivo: Caminho do arquivo CSV da agenda.
    :param id_evento: Identificador do evento que se quer alterar.
    :param nome_evnt: Novo nome do evento.
    :param data_evnt: Nova data do evento.
    :param hora_evnt: Novo horário do evento.
    :param descricao_evnt: Nova descrição do evento.
    :return:
    """

    agenda = ler_arquivo_agenda(nome_arquivo)

    i = 0
    encontrou_evento = False

    for i, evento in enumerate(agenda):
        if int(evento["id"]) == id_evento:
            if nome_evnt is None:
                nome_evnt = evento["nome"]
            if data_evnt is None:
                data_evnt = evento["data"]
            if hora_evnt is None:
                hora_evnt = evento["hora"]
            if descricao_evnt is None:
                descricao_evnt = evento["descricao"]
            encontrou_evento = True
            break

    if encontrou_evento:
        novo_evnt = {"id": str(id_evento),
                     "nome": nome_evnt,
                     "data": data_evnt,
                     "hora": hora_evnt,
                     "descricao": descricao_evnt}

        agenda[i] = novo_evnt

        escrever_arquivo_agenda(nome_arquivo, agenda)

        root_logger.info("Evento alterado:")
        root_logger.info("-----------------------------------------------")
        imprimir_info_evnt(novo_evnt, modo_logger=True)


def remover_evento(nome_arquivo: str, id_evento: int) -> None:
    """
    Remove um evento com o identificador especificado da agenda.

    :param nome_arquivo: Caminho do arquivo CSV da agenda.
    :param id_evento: Identificador do evento que se quer remover.
    :return:
    """

    agenda = ler_arquivo_agenda(nome_arquivo)

    for i, evento in enumerate(agenda):
        if int(evento["id"]) == id_evento:
            agenda.pop(i)
            break

    escrever_arquivo_agenda(nome_arquivo, agenda)
    root_logger.info(f"O evento {id_evento} foi removido com sucesso!")


def listar_eventos(nome_arquivo: str, data_evnt: str) -> None:
    """
    Lista todos os eventos da agenda para uma data especificada.

    :param nome_arquivo: Caminho do arquivo CSV da agenda.
    :param data_evnt: Data do evento.
    :return:
    """

    agenda = ler_arquivo_agenda(nome_arquivo)

    if data_evnt is None:
        # Uma shallow copy deve ser suficiente
        eventos_listados = agenda
    else:
        eventos_listados = list(filter(lambda x: x.__getitem__("data") == data_evnt, agenda))

    if len(eventos_listados) > 0:
        print(f"Eventos do dia {data_evnt}")
        print("-----------------------------------------------")
        for evento in eventos_listados:
            imprimir_info_evnt(evento)

    else:
        print(f"Não existem eventos para o dia {data_evnt}!")
        return


def imprimir_info_evnt(evento: EventoAgenda, modo_logger=False) -> None:
    info_evnt = (f'Evento {evento["id"]} - {evento["nome"]}\n'
                 f'Descrição: {evento["descricao"]}\n'
                 f'Data: {evento["data"]}\n'
                 f'Hora: {evento["hora"]}\n'
                 '-----------------------------------------------\n')

    if modo_logger:
        root_logger.info(info_evnt)
    else:
        print(info_evnt)


def ler_arquivo_agenda(nome_arquivo: str) -> Agenda:
    """
    Lê o arquivo CSV da agenda e retorna uma lista de eventos.

    :param nome_arquivo: Caminho do arquivo CSV.
    :return: Lista de eventos, onde cada evento é um dicionário cujas chaves são os rótulos das colunas, e os valores
    correspondem aos campos de cada registro do arquivo.
    """

    with open(nome_arquivo, mode='r', encoding="UTF-8", newline='') as csv_file:
        csv_reader = csv.DictReader(csv_file, dialect="agenda_de_eventos")
        agenda = list(csv_reader)

    return agenda


def escrever_arquivo_agenda(nome_arquivo: str, agenda: Agenda) -> None:
    """
    Escreve os dados da agenda no arquivo CSV especificado.

    :param nome_arquivo: Caminho do arquivo CSV da agenda.
    :param agenda: Lista de eventos da agenda.
    :return:
    """

    _HEADER = ["id", "nome", "data", "hora", "descricao"]

    with open(nome_arquivo, mode='w', encoding="UTF-8", newline='') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=_HEADER, dialect="agenda_de_eventos")
        csv_writer.writeheader()

        for evento in agenda:
            csv_writer.writerow(evento)
