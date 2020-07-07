def main():
    valor = int(input().replace('.', ''))

    notas = {10000: 0, 5000: 0, 2000: 0, 500: 0, 200: 0}
    imprime_notas = False

    moedas = {100: 0, 50: 0, 25: 0, 10: 0, 5: 0, 1: 0}
    imprime_moedas = False

    for nota in notas:
        n, valor = divmod(valor, nota)
        notas[nota] = n
        if n:
            imprime_notas = True

    for moeda in moedas:
        n, valor = divmod(valor, moeda)
        moedas[moeda] = n
        if n:
            imprime_moedas = True

    if imprime_notas:
        print("NOTAS:")
        for nota, n in notas.items():
            if n:
                print(f"{n} nota(s) de R$ {nota / 100:.2f}")

    if imprime_moedas:
        print("MOEDAS:")
        for moeda, n in moedas.items():
            if n:
                print(f"{n} moeda(s) de R$ {moeda / 100:.2f}")


if __name__ == '__main__':
    main()
