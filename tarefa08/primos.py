"""
Daniel Paulo Garcia © 2020

primos.py

Descrição: Recebe uma sequência de números inteiros positivos e retorna a soma dos quadrados dos números primos dessa
sequência.
"""

import math
from typing import Callable


def filtra(f: Callable, lista: list) -> list:
    """Filtra os elementos de uma lista retornando apenas os elementos para os quais o retorno de f é True"""
    nova_lista = []

    for elemento in lista:
        if f(elemento):
            nova_lista.append(elemento)

    return nova_lista


def mapeia(f: Callable, lista: list) -> list:
    """Aplica uma função f sobre cada elemento da lista e devolve uma nova lista"""
    nova_lista = []

    for elemento in lista:
        nova_lista.append(f(elemento))

    return nova_lista


def reduz(f: Callable, lista: list) -> int:
    """
    Recebe uma lista e uma função acumuladora que deve operar sobre o valor previamente acumulado e um elemento da
    lista. Retorna o valor acumulado ao percorrer todos os itens da lista.
    """
    valor_acumulado = 0
    i = 0

    while i < len(lista):
        valor_acumulado = f(valor_acumulado, lista[i])
        i += 1

    return valor_acumulado


def eh_primo(numero: int) -> bool:
    """Se o número for primo, retorna True. Caso contrário, retorna False."""
    if numero == 1:
        return False
    elif numero in (2, 3):
        return True
    elif numero % 2 == 0 or numero % 3 == 0:
        return False
    else:
        i = 6
        square_root = int(math.sqrt(numero))
        while i <= square_root:
            if numero % (i - 1) == 0 or numero % (i + 1) == 0:
                return False
            i += 6

        return True


def main():
    # Lê uma lista de números da entrada padrão e converte cada elemento para <int>
    entrada = input().split()
    entrada = [int(elemento) for elemento in entrada]

    entrada = filtra(eh_primo, entrada)
    entrada = mapeia(lambda x: x**2, entrada)

    resultado = reduz(lambda acumulado, valor: acumulado + valor, entrada)
    print(resultado)


if __name__ == '__main__':
    main()
