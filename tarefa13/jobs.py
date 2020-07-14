def dividir_trabalhos(n, graus):
    soma_esquerda = 0
    soma_direita = 0

    if n == 1:
        return graus[0]

    i, j = 0, n - 1
    while i <= j:
        if soma_esquerda <= soma_direita:
            soma_esquerda += graus[i]
            i += 1
        else:
            soma_direita += graus[j]
            j -= 1

    return abs(soma_esquerda - soma_direita)


def main():
    respostas = []
    try:
        while True:
            n = int(input())
            graus = tuple(int(dificuldade) for dificuldade in input().split())
            resposta = dividir_trabalhos(n, graus)
            respostas.append(resposta)
    except EOFError:
        for r in respostas:
            print(r)


if __name__ == '__main__':
    main()
