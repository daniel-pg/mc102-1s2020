from frequencia import calcular_quartis


def main():
    # TODO: No momento esses testes não funcionam, só estão aí de enfeite. Corrigir isso depois.
    teste1 = [7, 15, 36, 39, 40, 41]
    teste2 = [6, 7, 15, 36, 39, 40, 41, 42, 43, 47, 49]

    assert calcular_quartis(teste1) == (15, 37.5, 40)
    assert calcular_quartis(teste2) == (15, 40, 43)


if __name__ == '__main__':
    main()
