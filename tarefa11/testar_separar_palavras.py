from frequencia import separar_palavras


def main():
    texto = """Ciência da computação é a ciência que estuda as técnicas, metodologias, instrumentos computacionais e
aplicações tecnológicas, que automatizem os processos e desenvolvam soluções de processamento de dados de entrada 
e saída pautado no computador, de forma que se transforme em informação. Não se restringindo apenas ao estudo dos 
algoritmos, suas aplicações e implementação na forma de software. Assim, a Ciência da Computação também abrange 
as técnicas de modelagem de dados e gerenciamento de banco de dados, envolvendo também a telecomunicação e os 
protocolos de comunicação, além de princípios que abrangem outras especializações da área."""

    stop_words = ['é', 'e', 'a', 'as', 'o', 'os', 'que', 'de', 'da',  'dos', 'pautado', 'em', 'no', 'na', 'se', 'ainda',
                  'ao', 'não', 'apenas', 'suas', 'assim', 'também', 'além', 'outras']

    palavras = separar_palavras(texto, stop_words)

    assert palavras == ['ciência', 'computação', 'ciência', 'estuda', 'técnicas', 'metodologias', 'instrumentos',
                        'computacionais', 'aplicações', 'tecnológicas', 'automatizem', 'processos', 'desenvolvam',
                        'soluções', 'processamento', 'dados', 'entrada', 'saída', 'computador', 'forma', 'transforme',
                        'informação', 'restringindo', 'estudo', 'algoritmos', 'aplicações', 'implementação',
                        'forma', 'software', 'ciência', 'computação', 'abrange', 'técnicas', 'modelagem',
                        'dados', 'gerenciamento', 'banco', 'dados', 'envolvendo', 'telecomunicação', 'protocolos',
                        'comunicação', 'princípios', 'abrangem', 'especializações', 'área']


if __name__ == '__main__':
    main()
