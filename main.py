from src.car.edit import edit_car_by_id
from src.car.delete import delete_car_by_id
from src.car.display import display_all_cars, display_car_by_id
from database.seeder import seeder
from database.connection import open_connection
from src.interface.user_interface import main_menu
from src.enums.menu import Menu
from src.car.registry import register_car


def display_menu() -> None:
    main_menu()


def handle_option(option: str) -> bool:
    if option == Menu.REGISTRY_NEW_CAR.value:
        register_car(conn, cursor)
    elif option == Menu.DISPLAY_ALL_CARS.value:
        display_all_cars(conn, cursor)
    elif option == Menu.DISPLAY_CAR_BY_ID.value:
        display_car_by_id(conn, cursor)
    elif option == Menu.DELETE_CAR_BY_ID.value:
        delete_car_by_id(cursor, conn)
    elif option == Menu.EDIT_CAR_BY_ID.value:
        edit_car_by_id(cursor, conn)
    elif option == Menu.EXIT.value:
        print("\n---------------- Agradecemos por usar o nosso sistema ----------------\n")
        return False
    else:
        print("\nDigite uma opção válida!\n")

    return True

if __name__ == "__main__":
    #Abrindo uma conexão com o banco de dados
    conn, cursor = open_connection()
    #Populando o banco de dados caso não tenha sido feito
    is_seeded = seeder(conn, cursor)
    if is_seeded:
        print("Seeding já tinha sido aplicado!")
    print("Seeding completo com sucesso!")
    ##Exibe as opções disponiveis, no menu, para o usuário
    while True:
        display_menu()
        option = int(input("Digite a opção desejada: "))
        should_continue = handle_option(option)
        if not should_continue:
            break
    
    
    
    
















