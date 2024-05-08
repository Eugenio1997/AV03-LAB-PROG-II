from database.seeder import seeder
from database.connection import open_connection
from src.interface.user_interface import main_menu

# ------------ Bem vindo ao Carfolio ------------

# - O que deseja?

#   - Cadastrar um carro
#   - Listar os carros cadastrados
#   - Parar a execução do programa


def display() -> None:
    main_menu()


if __name__ == "__main__":
    #Abrindo uma conexão com o banco de dados
    conn, cursor = open_connection()
    #Populando o banco de dados caso não tenha sido feito
    is_seeded = seeder(conn, cursor)
    if is_seeded:
        print("Seeding já tinha sido aplicado!")
    print("Seeding completo com sucesso!")
    ##Exibe as opções disponiveis, no menu, para o usuário
    display()
    option = input("Digite a opção desejada: ")
    
    
    
    
















