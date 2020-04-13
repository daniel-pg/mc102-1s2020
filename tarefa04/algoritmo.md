# Descreva um algoritmo #
Descreva em português um algoritmo para resolver o problema descrito na tarefa.

## Entrada #
* Três baldes, identificados como A, B e C e com capacidades 2, 7 e 4 litros, respectivamente.
* Os volumes iniciais de água de cada balde, de maneira que os baldes A e C estão vazios, enquanto o balde B está cheio de água.

## Saída #
* Qualquer um dos baldes fornecidos na entrada, contendo apenas 1 litro de água.

## Conjunto de Instruções #
Uma vez que as entradas e saídas válidas já foram descritas precisamente, falta apenas descrever um conjunto de instruções a partir do qual o algoritmo será construído. Para isso, o operador deve ser capaz de: 

1. Despejar água de um balde para outro até completar sua capacidade.
2. Entregar um balde.


## Algoritmo #

```
() Despeje água do balde B no balde A até a borda;
() Despeje água do balde B no balde C até a borda;
() Entregue o balde B.
```
