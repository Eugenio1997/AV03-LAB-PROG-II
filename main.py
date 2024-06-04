from src.order.order import make_order
from src.enums.auth_menu import Auth_Menu
from src.enums.unauth_menu import Unauth_Menu
from src.car.edit import edit_car_by_id
from src.car.delete import delete_car_by_id
from src.car.display import display_all_cars, display_car_by_id
from database.seeder import seeder
from database.connection import open_connection
from src.interface.user_interface import (
    show_authenticated_menu,
    show_admin_menu,
    show_main_menu,
)
from src.enums.admin_menu import Admin_Menu
from src.car.registry import register_car
from src.user.login import (
    authenticate_user,
    get_authenticated_user_email,
    get_authentication_status,
    logout,
)
from src.user.registry import register_user
from src.utils import get_admin_user_email


def display_menu() -> int:
    if not get_authentication_status():
        return show_main_menu()
    elif (
        get_authentication_status()
        and get_authenticated_user_email() == get_admin_user_email()
    ):
        return show_admin_menu()
    elif get_authentication_status():
        return show_authenticated_menu()


def handle_option(option: str) -> bool:
    """
    Função para lidar com a opção escolhida pelo usuário
    """
    if not get_authentication_status():
        if option == Unauth_Menu.REGISTER.value:
            register_user(conn, cursor)
        elif option == Unauth_Menu.LOGIN.value:
            authenticate_user(conn, cursor)
        elif option == Unauth_Menu.EXIT.value:
            print("\nPrograma encerrado\n")
            return False
        else:
            print("\nDigite uma opção válida!\n")
    elif get_authentication_status():
        if option == Auth_Menu.DISPLAY_CARS.value:
            display_all_cars(conn, cursor)
        elif option == Auth_Menu.MAKE_ORDER.value:
            if make_order(conn, cursor) is False:
                back_to_main_menu = True
                return back_to_main_menu
        elif option == Auth_Menu.DISPLAY_CAR_BY_ID.value:
            display_car_by_id(conn, cursor)
        elif option == Auth_Menu.PROVA.value:
            print("Prova")
        elif option == Auth_Menu.LOGOUT.value:
            logout()
        else:
            print("\nDigite uma opção válida!\n")
    elif (
        get_authentication_status()
        and get_authenticated_user_email() == get_admin_user_email()
    ):
        if option == Admin_Menu.REGISTRY_NEW_CAR.value:
            register_car(conn, cursor)
        elif option == Admin_Menu.DISPLAY_ALL_CARS.value:
            display_all_cars(conn, cursor)
        elif option == Admin_Menu.DISPLAY_CAR_BY_ID.value:
            display_car_by_id(conn, cursor)
        elif option == Admin_Menu.DELETE_CAR_BY_ID.value:
            delete_car_by_id(cursor, conn)
        elif option == Admin_Menu.EDIT_CAR_BY_ID.value:
            edit_car_by_id(cursor, conn)
        elif option == Admin_Menu.EXIT.value:
            print(
                "\n---------------- Agradecemos por usar o nosso sistema ----------------\n"
            )
            return False

    return True


if __name__ == "__main__":
    # Abrindo uma conexão com o banco de dados
    conn, cursor = open_connection()
    # Populando o banco de dados caso não tenha sido feito
    is_seeded = seeder(conn, cursor)
    if is_seeded:
        print("Seeding já tinha sido aplicado!")
    print("Seeding completo com sucesso!")
    ##Exibe as opções disponiveis, no menu, para o usuário

    while True:
        option = display_menu()
        should_continue = handle_option(option)
        if not should_continue:
            break
