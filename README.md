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

É possível adicionar novas receitas, visualizar, alterar receitas e estatísticas gerais. Bem como calcular custos e visualizá-los por meio de um arquivo CSV, o qual também traz informações sobre quais seriam as receitas mais caras e mais baratas.

## 4. Dificuldades

O projeto se mostrou bastante desafiador inicialmente dada a sua proximidade com um problema real. Diante disso, precisamos assumir algumas restrições ao problema, limitando a um conjunto de dados que estivesse dentro do padrão esperado para este módulo. Após trazer o projeto para um escopo mais simples, tivemos algumas dificuldades com relação a implementação de códigos, as quais podemos citar as seguintes: construção das funções min e max, salvar os resultados em abas diferentes no csv, complexidade da função alterar considerando um dicionário dentro de um dicionário e filtrar os dados. Apesar disso, o resultado obtido para uma primeira versão do produto é bastante satisfatório e diversos pontos oportunistas para versões futuras. 

## 5. Créditos e contribuições

* Camila Stavola - Construção do arquivo .json, função de calcula custo total das receitas. Diversas contribuições no escopo do projeto;

* Jéssica Moreira - Elaboração da função custo total por receita, construção inicial das funções min e max e exportação para csv;

* Lavínia Beatriz - Funções responsáveis por atualizar a lista de receitas e deletar algum elemento, menu principal e auxílio nos dados estatísticos;

* Lucas Fernando - Estrutura geral do projeto, funções de carregamento de arquivo, leitura de dados do arquivo e algumas atualizações gerais em outras funções;
  
* Rodrigo Ventura - Criou o Readme.
