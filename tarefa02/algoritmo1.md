# Somar duas datas #
Uma vez definidas as entradas e a saída do algoritmo, devemos definir um conjunto mínimo de instruções necessárias para que, quando executadas em certa ordem em particular, convertam qualquer entrada válida em uma saída também válida para esta entrada.

## Conjunto de Instruções #
1. Ler valores da entrada.
2. Armazenar, sobrescrever, indexar, nomear e ler valores na memória.
3. Devolver um valor para a saída.
4. Somar, subtrair, dividir ou multiplicar dois números quaisquer.
5. Calcular o resto da divisão de dois números inteiros.
6. Interpretar e executar desvios condicionais
7. Interpretar e executar iterações limitadas ou condicionais
8. Definir e executar sub-rotinas, passar parâmetros e retornar valores.



## Algoritmo #

```
() Definir a sub-rotina Nº_DE_DIAS_DO_MES(X):
    (.) Se X for igual a 0, retorne o valor 0
    (.) Se X for igual a 02, retorne o valor 28
    (.) Se X for igual a 04, 06, 09 ou 11, retorne o valor 30
    (.) Retorne o valor 31

() Definir a sub-rotina É_ANO_BISSEXTO(X):
    (.) Se o resto da divisão de X por 400 for igual a zero, retorne verdadeiro.
    (.) Se o resto da divisão de X por 4 for igual a zero E  
    o resto da divisão de X por 100 for diferente de zero, retorne verdadeiro.
    (.) Retorne falso.

() Ler os valores dia_1, mês_1 ano_1 da entrada e armazenar na memória.
() Ler os valores dia_2, mês_2 ano_2 da entrada e armazenar na memória.
() Enquanto ano_2 for maior ou igual a zero, faça:
    (.) Enquanto mês_2 for maior que zero, faça:
        (..) Some dia_1 e dia_2, e armazene o resultado em dia_1.
        (..) Subtraia mês_2 de uma unidade, e armazene o resultado em mês_2.
        (..) Calcule Nº_DE_DIAS_DO_MES(mês_2) e armazene em dia_2.
        (..) Se É_ANO_BISSEXTO(ano_2) for verdadeiro e mês_2 for igual a 02, faça:
            (...) Some uma unidade a dia_2, e armazene o resultado em dia_2.
    (.) Subtraia ano_2 de uma unidade, e armazene o resultado em ano_2.
    (.) Armazene o valor 12 em mês_2.
() Enquanto dia_1 for maior que Nº_DE_DIAS_DO_MES(mês_1), faça:
    (.) Subtraia dia_1 de Nº_DE_DIAS_DO_MES(mês_1 + 1), e armazene o resultado em dia_1.
    (.) Se É_ANO_BISSEXTO(ano_1) for verdadeiro e (mês_1 + 1) for igual a 02, faça:
        (..) Subtraia uma unidade de dia_1, e armazene o resultado em dia_1.
    (.) Some uma unidade a mês_1, e armazene o resultado em mês_1.
    (.) Se mês_1 for maior que 12, faça:
        (..) Subtraia mês_1 de doze unidades, e armazene o resultado em mês_1.
        (..) Some uma unidade a ano_1, e armazene o resultado em ano_1.
() Armazenar na memória o valor dia_3, e definir como sendo igual a dia_1.
() Armazenar na memória o valor mês_3, e definir como sendo igual a mês_1.
() Armazenar na memória o valor ano_3, e definir como sendo igual a ano_1.
() Devolver os valores dia_3, mês_3 e ano_3 para a saída.
```
