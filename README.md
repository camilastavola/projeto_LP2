# Projeto de Gerenciamento de Dados - Receitas 📋🍳

## Índice

1. Requisitos
2. Introdução
3. Uso do projeto
4. Dificuldades
5. Créditos e contribuições

## 1. Requisitos

a. Leitura de Dados: Desenvolva um componente capaz de ler uma lista de objetos contidos em um arquivo JSON, representando informações sobre tema escolhidoes.

b. Mapeamento, Filtro e Redução: Implemente funcionalidades para realizar mapeamento, filtragem e redução dos dados, proporcionando uma análise mais refinada das informações contidas no conjunto de dados.

c. Manipulação de Dados Individuais: Permita a leitura individual, atualização e exclusão de do arquivos, mantendo o arquivo JSON sempre atualizado.

d. Validações de Operações: Integre validações utilizando blocos try-except e raise para garantir a robustez das operações, prevenindo erros e assegurando a consistência dos dados.

e. Obtenção de Estatísticas Simples: Desenvolva uma função para extrair dados estatísticos simples, como média, máximo e mínimo, por exemplo, aum item X nos dados de exatas.

f. Identificação de Máximos/Mínimos com Detalhes: Crie uma função que retorne uma lista de tuplas, contendXdo professor e o valor máximo (ou mínimo) de algum atributo numérico. Esta função deve ser configurável para fornecer estatísticas de máximo ou mínimo.

g. Exportação de Dados Estatísticos para CSV: Implemente a capacidade de salvar os dados estatísticos obtidos em um arquivo CSV, permitindo uma análise posterior ou compartilhamento fácil dos resultados.

## 2. Introdução

O projeto final do módulo de Lógica de Programação II foi uma maneira muito interessante de fazermos a conexão dos fundamentos da linguagem de programação que estudamos - o Python - com aplicações práticas em um projeto de gerenciamento de dados de receitas, construindo uma aplicação em Python que oferece uma variedade de funcionalidades para manipulação e análise de dados relacionados a receitas culinárias. Com ela é possível adicionar novas receitas, visualizar receitas existentes, alterar detalhes das receitas e calcular os custos associados aos ingredientes de cada receita.

## 3. Uso do Projeto

É possível adicionar novas receitas, visualizar, alterar receitas e estatísticas gerais. Bem como calcular custos.

## 4. Dificuldades

Descrever as dificuldades.
Tivemos dificuldade na construção das funções min e max de forma a salvar os resultados em abas diferentes no csv, pois, ao salvar aparecia o erro de que não era possível salvar dados de tipos diferentes. Já que o resultado retornava o nome da receita, no formato string, e o custo, no formato float. Lucas conseguiu chegar na solução do problema.

## 5. Créditos e contribuições

Rodrigo Ventura - criou o Read Me

Camila Stavola - 

Jéssica Moreira - Elaboração da função custo total por receita, construção inicial das funções min e max e exportação para csv.

Lavínia Beatriz - funções responsáveis por atualizar a lista de receitas e deletar algum elemento, menu principal e auxílio no processamentos dos dados estatísticos 

Lucas Fernando - 
