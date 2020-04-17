# lê uma string com três partes
a, b, c = input().split()

# converte strings em números
a = float(a)
b = float(b)
c = float(c)

# termine esse programa aqui...

# Igualdades com números de ponto flutuante exigem uma margem de erro:
epsilon = 6.0e-17

def eh_triangulo_retangulo(aa, bb, cc):
    if abs(aa - bb - cc) < epsilon or \
            abs(bb - aa - cc) < epsilon or \
            abs(cc - aa - bb) < epsilon:
        return True
    else:
        return False

def eh_triangulo_obtusangulo(aa, bb, cc):
    if (aa - bb - cc) > 0 or \
            (bb - aa - cc) > 0 or \
            (cc - aa - bb) > 0:
        return True
    else:
        return False

# Condição de existência de um triângulo
if (abs(a - b) < c + epsilon < (a + b)):

    # Pré-computar os quadrados das variáveis
    aa = a**2
    bb = b**2
    cc = c**2

    if eh_triangulo_retangulo(aa, bb, cc):
        print("retângulo")
    elif eh_triangulo_obtusangulo(aa, bb, cc):
        print("obtusângulo")
    else:
        print("acutângulo")

else:
    print("não forma triângulo")