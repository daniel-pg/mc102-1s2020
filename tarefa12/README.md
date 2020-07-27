# Agenda
## Introdução
Trata-se de uma pequena aplicação CLI para gerenciamento de agendas. Cada agenda contém uma lista de eventos salvos pelo
usuário, onde cada evento é composto por um identificador, nome, data, hora e descrição.

## Como usar
O programa opera sobre um arquivo de agenda, que deve ser especificado através do parâmetro `-a <agenda>`. É possível
realizar 5 tipos de operações diferentes:

1. `inicializar`: Cria uma nova agenda vazio no caminho especificado, contendo apenas o cabeçalho. Ex.:  
`agenda.py -a agenda.csv inicializar`

2. `criar`: Cria um novo evento com as informações dadas. Ex.:  
`agenda.py -a agenda.csv criar --nome MC102 --data 01/01/2020 --hora 14:00 --descricao "Aula de laboratório"`

3. `alterar`: Altera um evento dado o seu identificador, substituindo os valores antigos pelos novos. Se um novo valor
não for especificado, mantém o original. Ex.:  
`agenda.py -a agenda.csv alterar --evento 1 --hora 16:00`

4. `remover`: Remove um evento, dado o seu identificador. Ex.:  
`agenda.py -a agenda.csv remover --evento 7`

5. `listar`: Lista todos os eventos da data fornecida. Ex.:  
`agenda.py -a agenda.csv listar --data 13/06/2020`


Para ver a ajuda do programa, digite no terminal:  
``agenda.py -h``  
Para obter uma lista com todos os parâmetros aceitos por um comando específico, digite:  
``agenda.py <operação> -h``


## Formato do arquivo
As agendas são salvas em arquivos CSV, codificados em texto UTF-8, cujo formato está descrito a seguir:  
* A primeira linha contém um **cabeçalho**, cujos elementos representam os nomes ou **rótulos** dos campos de dados
dos registros (**colunas**), na ordem em que aparecem. Cada elemento do cabeçalho deve ser separado dos outros por uma
vírgula.

* O cabeçalho deve conter exatamente estes cinco rótulos: `id`, `nome`, `data`, `hora` e `descricao`.  
Note que, apesar do programa inicializar a agenda com os elementos do cabeçalho nessa ordem, qualquer outra ordem dos
rótulos seria igualmente válida, observada a sequência correta das colunas dos registros.

* A linhas subsequentes do arquivo representam **registros**, sendo que cada linha deve conter um único registro e
terminar com um caractere Line-feed (LF). Contudo, um registro pode conter uma quebra de linha embutida.

* Cada registro contém uma série de **campos** de dados, que também devem ser separados por vírgulas. Exemplo:  
``1,MC102,01/01/2020,14:00,Aula de laboratório``

* Espaços adjacentes às vírgulas separadoras, à esquerda ou à direita, serão ignorados.

* Campos contendo vírgulas ou quebras de linha embutidas, ou espaços no início ou no final, devem ser delimitados por
aspas duplas.

* Campos que contenham aspas duplas devem ser delimitados por aspas duplas, e todas as ocorrências das aspas dentro do
campo devem ser substituídas por um par de aspas.

* Os campos sempre podem ser delimitados por aspas duplas, mesmo nos casos opcionais. Elas serão descartadas em qualquer
caso.

## Estrutura de dados da agenda
A agenda é uma coleção de eventos que, no Python, pode ser representada como uma lista de dicionários. Cada dicionário
da lista representa o **registro** de um evento, onde suas chaves são os **rótulos** e os valores são os **campos**.
