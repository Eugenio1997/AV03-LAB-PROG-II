## AV03 LAB PROG II

Este repositório contém o código-fonte para a Avaliação 03 da disciplina de Laboratório de Programação 2.

## Descrição

O projeto consiste em um sistema de gerenciamento de carros, onde os usuários podem cadastrar diferentes tipos de carros, listar os carros cadastrados e recuperar um determinado carro pelo ID.

## Tecnologias Utilizadas

- Python 3.10.1: Linguagem de programação utilizada para desenvolver o sistema.
- Git 2.42.0: Sistema de controle de versão utilizado para gerenciar o código-fonte do projeto.
- Prettytable 3.10.0: Biblioteca Python utilizada para formatar e exibir os dados em formato tabular.
- Wcwidth 0.2.13: Biblioteca Python para medir a largura de caracteres de largura fixa.
- Sqlite 3.35.5: Banco de dados embutido utilizado para armazenar os dados dos carros cadastrados.
- Faker (versão 25.0.1) - Uma biblioteca Python que gera dados falsos.
- python-dateutil (versão 2.9.0.post0) - Uma biblioteca Python para análise, manipulação e trabalho com datas e horas.
- Six (versão 1.16.0) - Uma biblioteca de compatibilidade Python 2 e 3 que fornece utilitários para escrever código compatível com Python 2 e Python 3.

## Funcionalidades

- Cadastrar carro: Permite aos usuários cadastrar um novo carro, fornecendo informações como tipo, modelo, ano e potência.
- Listar carros cadastrados.
- Recuperar carro por ID


## Como Usar

Ao executar o programa, siga as instruções exibidas no console para realizar as seguintes operações:


**Tela do Menu Principal**


------------ Bem vindo ao Carfolio ------------

- O que deseja?

  - Cadastrar um carro (1)
  - Listar os carros cadastrados (2)
  - Exibir carro pelo ID (3)
  - Parar a execução do programa (4)

**Tela de Cadastrar Carro:**

------------ Realizando o cadastro de um novo carro ------------

1- Qual é o tipo do carro ?

  - Sedan (1)
  - Hatchback (2)
  - SUV (3)
  - Picape (4)
  - Minivan (5)
  - Esportivo (6)

2- Qual é a potência do carro ?
  
  - <Entrada-do-usuário>

3- Qual é o ano do carro ?

  - <Entrada-do-usuário>

4- Quantas portas o carro possui ?

  - <Entrada-do-usuário>

**Tela de Exibição dos Carros Cadastrados:**

| Tipo          | Ano | Quantidade de Portas | Potência |
|---------------|-----|----------------------|----------|
| Sedan         | 2022| 4                    | 180 hp   |
| Hatchback     | 2023| 5                    | 150 hp   |
| SUV           | 2024| 4                    | 200 hp   |
| Coupé         | 2022| 2                    | 250 hp   |
| Convertible   | 2023| 2                    | 220 hp   |
| Pickup Truck  | 2024| 4                    | 300 hp   |


**Tela de Recuperação de Carro por ID:**

  - Qual é o ID do carro que deseja visualizar ?

    - <Entrada-do-usuário>

**Tela de Exibição do Carro Cadastrado cujo ID é -ID-INSERIDO-PELO-USUARIO-:**

| Tipo          | Ano | Quantidade de Portas | Potência |
|---------------|-----|----------------------|----------|
| Sedan         | 2022| 4                    | 180 hp   |


## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para enviar pull requests com melhorias, correções de bugs ou novas funcionalidades.

## Colaboradores

- [Eugenio Lopes](https://github.com/Eugenio1997).


## Licença

Este projeto está licenciado sob a [MIT License](https://opensource.org/licenses/MIT).
