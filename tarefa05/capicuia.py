'''
Daniel Paulo Garcia © 2020

capicuia.py

Descrição: Lê um número inteiro positivo de 4 dígitos da entrada padrão e
verifica se esse número é capicua, ou seja, um número palíndromo.

Não é permitido o uso de comandos iterativos, como o while e o for.
'''

# Solução da malandragem:
# entrada = input()
# print("sim") if entrada[-1::-1] == entrada else print("não")


# Solução normal:
entrada = input()
n_de_algarismos = len(entrada)

if n_de_algarismos == 1:
    print("sim")
elif n_de_algarismos == 2 and entrada[0] == entrada[1]:
    print("sim")
elif n_de_algarismos == 3 and entrada[0] == entrada[2]:
    print("sim")
elif n_de_algarismos == 4 and entrada[0] == entrada[3] and entrada[1] == entrada[2]:
    print("sim")
else:
    # Note que isso inclui os casos em que o número de algarismo é maior que 4 (entrada inválida)
    print("não")
