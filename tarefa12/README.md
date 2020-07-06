# Agenda
## Introdução
Trata-se de uma pequena aplicação de interface de linha de comando (ILC) para gerenciamento de agendas. Cada arquivo de 
agenda contém uma lista de eventos salvos pelo usuário, onde cada evento é composto por um identificador, nome, data,
hora e descrição. As funções disponíveis no programa estão descritas a seguir. 

## Como usar
O programa opera sobre um arquivo de agenda, que deve ser especificado através do parâmetro `-a <agenda>`.
É possível realizar 5 tipos de operações diferentes sobre a agenda:
1. `inicializar`: Cria um novo arquivo de agenda vazio no caminho especificado, contendo apenas o
cabeçalho.
2. `criar`: Cria um novo evento com as informações dadas nos parâmetros.
3. `alterar`: Altera um evento dado o seu identificador, substituindo os valores antigos pelos novos. Se um novo valor
não for especificado, mantém o original.
4. `remover`: Remove um evento, dado o seu identificador.
5. `listar`: Lista todos os eventos de um dia na data fornecida.

Para ver a ajuda do programa, digite no terminal:  
``python agenda.py -h``  
Para obter uma lista com todos os parâmetros aceitos por um comando específico, digite:  
``python agenda.py <operação> -h``


## Formato do arquivo
As agendas são salvas em arquivos CSV (comma-separated values), codificados como um texto UTF-8, cujo formato está
descrito a seguir:  
* A primeira linha deve conter um **cabeçalho**, onde cada elemento representa o nome ou **rótulo** dos campos de dados
dos registros (**colunas**), na ordem em que aparecem. Cada elemento do cabeçalho deve ser separado dos outros por uma
vírgula.

* O cabeçalho deve conter exatamente estes cinco rótulos: `id`, `nome`, `data`, `hora` e `descricao`.  
Note que, apesar do programa inicializar a agenda com os elementos do cabeçalho na ordem em que foram citados, qualquer
outra ordem dos rótulos seria igualmente válida, observada a sequência correta das colunas dos registros.

* A linhas subsequentes do arquivo representam **registros**, sendo que cada linha deve conter um único registro. A linha
deve terminar com um caractere Line-feed (LF), no entanto um registro pode conter uma quebra de linha embutida, conforme
será discutido mais a frente.

* Cada registro contém uma série de **campos** de dados, que também devem estar separados por uma vírgula. Exemplo:  
``1,MC102,01/01/2020,14:00,Aula de laboratório``

* Espaços adjacentes às vírgulas separadoras de campos, à esquerda ou à direita, serão ignorados.

* Campos contendo vírgulas ou quebras de linha embutidas, ou espaços no início ou no final, devem ser delimitados por
aspas duplas.

* Campos que contenham aspas duplas devem ser delimitados por aspas duplas, e todas as ocorrências das aspas dentro do
campo devem ser substituídas por um par de aspas.

* Os campos sempre podem ser delimitados por aspas duplas, mesmo nos casos opcionais. Elas serão descartadas em qualquer
caso.

## Estrutura de dados da agenda
A agenda é uma coleção de eventos que, no Python, pode ser representada como uma lista de dicionários. Cada dicionário
da lista representa o **registro** de um evento, onde suas chaves são os **rótulos** e os valores são os **campos**.
