"""
Daniel Paulo Garcia © 2020

collatz.py

Descrição: Dado um número inteiro positivo, determina o número de repetições do procedimento descrito na conjectura de
Collatz (modificada na tarefa) para chegar em 1.
"""


def calcular_collatz(n, iteracoes):

    if n == 1:
        return iteracoes

    elif n % 2 == 0:
        n //= 2

    else:
        n = (3*n + 1) // 2

    iteracoes += 1
    return calcular_collatz(n, iteracoes)


def main():
    n = int(input())
    resultado = calcular_collatz(n, 0)
    print(resultado)


if __name__ == '__main__':
    main()
