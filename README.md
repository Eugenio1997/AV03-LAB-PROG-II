## AV03 LAB PROG II

Este repositório contém o código-fonte para a Avaliação 03 da disciplina de Laboratório de Programação 2.

## Descrição

Aplicação de gerenciamento de vendas de carros. A aplicação utiliza um banco de dados SQLite para armazenar informações sobre usuários, carros, pedidos e itens de pedido.

Os usuários são registrados na tabela de usuários com detalhes como nome, email e senha (hash). Eles podem fazer pedidos de carros, que são registrados na tabela de pedidos, contendo informações como o ID do usuário que fez o pedido, o status do pedido (pendente, concluído ou cancelado), o preço total e a quantidade total de carros no pedido.

Os carros disponíveis para compra são registrados na tabela de carros, com detalhes como tipo de carro, número de portas, potência, preço e ano de fabricação. Cada pedido pode conter vários itens de pedido, registrados na tabela de itens de linha, onde cada item de linha está associado a um pedido e a um carro, e contém a quantidade de carros solicitados e o preço total para esse item.

Além disso, há uma tabela de configuração que controla se o banco de dados foi inicialmente populado com dados falsos. Isso indica que a aplicação pode ser usada tanto para fins de desenvolvimento quanto de produção.

Em resumo, o sistema fornece uma plataforma para os usuários navegarem, fazerem pedidos de carros e administrarem suas compras.


## Tecnologias Utilizadas

- Python 3.10.1: Linguagem de programação utilizada para desenvolver o sistema.
- Git 2.42.0: Sistema de controle de versão utilizado para gerenciar o código-fonte do projeto.
- Prettytable 3.10.0: Biblioteca Python utilizada para formatar e exibir os dados em formato tabular.
- Wcwidth 0.2.13: Biblioteca Python para medir a largura de caracteres de largura fixa.
- Sqlite 3.35.5: Banco de dados embutido utilizado para armazenar os dados dos carros cadastrados.
- Faker (versão 25.0.1) - Uma biblioteca Python que gera dados falsos.
- python-dateutil (versão 2.9.0.post0) - Uma biblioteca Python para análise, manipulação e trabalho com datas e horas.
- Six (versão 1.16.0) - Uma biblioteca de compatibilidade Python 2 e 3 que fornece utilitários para escrever código compatível com Python 2 e Python 3.

## Instalação

1. Clone o repositório para o seu computador:

   - git clone https://github.com/Eugenio1997/AV03-LAB-PROG2.git
  

2. Navegue até o diretório do projeto:

   - cd AV03-LAB-PROG2

3. Execute o programa:

   - python main.py


## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para enviar pull requests com melhorias, correções de bugs ou novas funcionalidades.

## Colaboradores

- [Eugenio Lopes](https://github.com/Eugenio1997).

## Licença

Este projeto está licenciado sob a [MIT License](https://opensource.org/licenses/MIT).
