# Tarefa 03 #
Dados n números, encontrar aquele que possui o maior número de divisores.

## Entrada #
Conjunto de n números inteiros positivos.

## Saída #
Algum número da entrada que contiver o maior número de divisores. Se houver vários números com a mesma quantidade de divisores, então a saída pode ser qualquer um deles. Se a entrada contiver o número zero, o saída também é zero, pois possui infinitos divisores inteiros.

## Conjunto de instruções #
1. Ler valores da entrada.
2. Armazenar, ler, indexar, nomear e declarar valores e variáveis na memória.
3. Devolver um valor para a saída.
4. Somar, subtrair, dividir ou multiplicar dois números quaisquer.
5. Calcular o resto da divisão de dois números inteiros.
6. Interpretar e executar desvios condicionais.
7. Interpretar e executar iterações limitadas ou condicionais.
8. Definir e executar sub-rotinas, passar parâmetros e retornar valores.
9. Contar o número de itens de uma lista.

## Algoritmo #

```
() Definir a sub-rotina NUMERO_DE_DIVISORES(X):
    (.) Se X for igual a 1, retorne o valor 1.
    (.) Armazenar o valor 0 numa variável chamada "numero_de_divisores".
    
    (.) Armazenar o valor 1 numa variável chamada "j".
    (.) Enquanto j for menor ou igual a X, faça:
        (..) Se o resto da divisão de X por j for zero, faça:
            (...) Incremente o valor de "numero_de_divisores" em uma unidade.
        (..) Incremente o valor de j em uma unidade.
    (.) Retorne o valor de "numero_de_divisores".

() Ler valores da entrada e guardar numa lista nomeada "lista_de_numeros".
() Contar o número de itens da lista "lista_de_numeros" e guardar o valor na
variável nomeada "tamanho_da_lista". 
() Armazenar o valor 1 numa variável chamada "resultado".

() Armazenar o valor 1 numa variável chamada "i".
() Enquanto i for menor ou igual a tamanho_da_lista, faça:
    (.) Indexar o i-ésimo valor da lista "lista_de_numeros" e guarda na variável chamada "n".
    (.) Se n for igual a zero, armazene o valor de n em "resultado" e termine a execução do loop.
    (.) Se NUMERO_DE_DIVISORES(n) for maior que NUMERO_DE_DIVISORES(resultado), faça:
        (..) Armazene o valor de "n" na variável "resultado".
    (.) Incremente i em uma unidade.
() Devolver o valor de "resultado" para a saída. 
```
