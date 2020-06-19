from frequencia import calcular_quartis


def main():
    # TODO: No momento esses testes não funcionam, só estão aí de enfeite. Corrigir isso depois.
    teste1 = [('basquete', 11), ('futebol', 9), ('handebol', 8), ('vôlei', 7), ('xadrez', 5), ('tênis', 4),
              ('corrida', 3), ('natação', 1)]

    teste2 = [('açaí', 12), ('carambola', 11), ('cajá', 10), ('jabuticaba', 9), ('acerola', 8), ('manga', 8),
              ('maracujá', 8), ('jaca', 5), ('romã', 5), ('jamelão', 4), ('caju', 3), ('cupuaçu', 2), ('caqui', 2)]

    assert calcular_quartis(teste1) == (9, 7, 3)
    assert calcular_quartis(teste2) == (10, 8, 3)


if __name__ == '__main__':
    main()
