# Ler valores da entrada
lista_a = input().split()
lista_b = input().split()

# Variáveis auxiliares
saida = ""

def eliminar_elementos_repetidos(lista):
    k = len(lista) - 1
    nova_lista = []
    while k >= 0:
        if lista[k] not in lista[:k]:
            nova_lista.append(lista[k])
        k -= 1
    return nova_lista[-1::-1]

lista_a = eliminar_elementos_repetidos(lista_a)
lista_b = eliminar_elementos_repetidos(lista_b)

for i in lista_a:
    if i in lista_b:
        saida += i
        saida += " "

print(saida)