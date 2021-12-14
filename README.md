# Avaliação técnica

A proposta dessa avaliação é um problema em que o candidato possa fazer entregas parciais, a depender da disponibilidade de tempo e conhecimento técnico do mesmo. O foco do teste é avaliar as seguintes competências, na seguinte ordem de prioridade:

1. Qualidade de código em geral: desacoplamento, organização, testes, observabilidade, etc...
2. Modelagem de banco de dados relacional.
3. Conhecimento em sistemas web.
4. Arquitetura de solução de novos sistemas.
5. Conhecimento em AWS.

**Importante**: não há necessidade de *overengineering* da arquitetura para a solução do teste, ela pode ser feita da forma mais simples possível para atender os requisitos funcionais. Discussões de arquitetura de solução serão feitas na entrevista técnica posterior.

Com essas prioridades em mente, o candidato pode focar nesses aspectos ao desenvolver a solução. Os detalhes do problemas e as entregas serão detalhadas abaixo.

## Arquivo de documentos

Suponha um arquivo `.csv` de documentos exportados por um sistema, com os seguintes campos:

* `nome`: alfanumérico com o nome do cliente
* `sexo`: char com duas opções de valor ([M]asculino e [F]eminino)
* `nascimento`: data no formato [UTC](https://www.w3.org/TR/NOTE-datetime), por exemplo 13/12/2021 é representado como 2021-12-13
* `documento`: numérico com o número do documento
* `tipo_documento`: tipo de documento do cliente, podendo ser uma das seguintes opções: [A, B, C, D, E, F]

Um cliente é identificado pela seguinte chave: `nome`, `sexo` e `nascimento`. Caso possua mais de um documento registrado, há duas linhas para o mesmo cliente. Abaixo, um exemplo de cliente com mais de um documento:

|     | nome                                               | sexo   | nascimento          |       documento | tipo_documento   |
|----:|:---------------------------------------------------|:-------|:--------------------|----------------:|:-----------------|
| 390 | OSOLZGMLZIRNZPFJRRFZRZFQPEZXYDQLFKKNMOPFTUIRYXSZYX | M      | 2008-09-23 00:00:00 | 952455741800658 | A                |
| 391 | OSOLZGMLZIRNZPFJRRFZRZFQPEZXYDQLFKKNMOPFTUIRYXSZYX | M      | 2008-09-23 00:00:00 | 982313953196615 | B                |

O arquivo exportado é uma extração completa, com a "foto" do estado atual da base de dados.

## Problema

Gostaríamos de um sistema que armazenasse os dados desse arquivo, de forma que seja possível olhar para dados do passado e identificar as mudanças que ocorreram. Um documento no arquivo pode sofrer as seguintes modificações:

**Remoção**: o documento é simplesmente apagado, não está mais presente no arquivo.

Arquivo original:

|    | nome                                               | sexo   | nascimento   |       documento | tipo_documento   |
|---:|:---------------------------------------------------|:-------|:-------------|----------------:|:-----------------|
|  0 | VCNJNMNJBENRYPBFVZIRXQXQDCRPWJQFCYENJQXDOTIHCWPFFR | F      | 1991-02-10   | 004602004239288 | A                |

Arquivo novo:

| nome   | sexo   | nascimento   | documento   | tipo_documento   |
|--------|--------|--------------|-------------|------------------|


**Adição**: há um novo registro de documento cadastrado para um mesmo cliente.

Arquivo original:

|    | nome                                               | sexo   | nascimento   |       documento | tipo_documento   |
|---:|:---------------------------------------------------|:-------|:-------------|----------------:|:-----------------|
|  9 | CSURXNYOHGQEXHZRGBGTVTXUDVWKCQIDRLYJONCMCTEFDFONID | M      | 2002-08-31   | 526990138144015 | A                |

Arquivo novo:

|    | nome                                               | sexo   | nascimento   |       documento | tipo_documento   |
|---:|:---------------------------------------------------|:-------|:-------------|----------------:|:-----------------|
|  9 | CSURXNYOHGQEXHZRGBGTVTXUDVWKCQIDRLYJONCMCTEFDFONID | M      | 2002-08-31   | 526990138144015 | A                |
|  9 | CSURXNYOHGQEXHZRGBGTVTXUDVWKCQIDRLYJONCMCTEFDFONID | M      | 2002-08-31   | 505740331208463 | E                |

**Atualização**: um documento mantém o mesmo `tipo_documento`, mas o valor do campo `documento` é modificado.

Arquivo original:

|    | nome                                               | sexo   | nascimento   |       documento | tipo_documento   |
|---:|:---------------------------------------------------|:-------|:-------------|----------------:|:-----------------|
| 18 | BVRXIKIIZMLIVBUSLPNGFMYCBPLZBTEGQJFLWWEIQLHVSYDHKV | F      | 2002-05-05   | 974840526508608 | A                |
| 19 | BVRXIKIIZMLIVBUSLPNGFMYCBPLZBTEGQJFLWWEIQLHVSYDHKV | F      | 2002-05-05   | 867878830360049 | B                |

Arquivo novo:

|    | nome                                               | sexo   | nascimento   |       documento | tipo_documento   |
|---:|:---------------------------------------------------|:-------|:-------------|----------------:|:-----------------|
| 18 | BVRXIKIIZMLIVBUSLPNGFMYCBPLZBTEGQJFLWWEIQLHVSYDHKV | F      | 2002-05-05   | 974840526508608 | A                |
| 19 | BVRXIKIIZMLIVBUSLPNGFMYCBPLZBTEGQJFLWWEIQLHVSYDHKV | F      | 2002-05-05   | 824818441205015 | B                |

## Entregáveis

Há dois arquivos de exemplo, um chamado `arquivo_original.csv` e outro `arquivo_novo.csv`. O primeiro é uma carga inicial, o segundo arquivo é uma carga com as modificações descritas acima. Trabalhando com esses arquivos de exemplos, esperamos as seguintes entregas:

### Entrega mínima

* Modelagem relacional e banco de dados no SGBD de preferência (*e.g.* SQLite, SQL Server, MySQL)
* Aplicação que faça a leitura dos arquivos, persista no banco de dados e gere o relatório de mudanças. Utilizaremos ambiente .NET e Java, mas o candidato pode usar outra linguagem a combinar.
* Implementar testes unitários na aplicação.

### Entrega desejada

* Implementar um front-end para a subida dos arquivos e apresentação dos resultados.
* Solução disponibilizada em container Docker.

### Entrega extras

* Implementar a solução do front-end como SPA e framework Angular.
* Deploy da solução em ambiente AWS.
* Esteira de CI/CD: execução automatizada de testes, automação de build, verificação de qualidade de código (e.g. Sonarqube) e ferramentas de observabilidade.

