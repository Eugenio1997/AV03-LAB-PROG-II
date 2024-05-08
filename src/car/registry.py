import sqlite3
from dao.car_dao import insert_car_into_database
from src.enums.car_types import get_member_name
from src.models.car_model import Car, create_car


def register_car(conn: sqlite3.Connection, cursor: sqlite3.Cursor) -> None:
    """ "
    Realiza o cadastro do carro na database
    """
    new_car = get_user_car_data()
    insert_car_into_database(new_car, conn, cursor)


def get_user_car_data() -> Car:
    """
    Retorna um objeto Car com os dados inseridos pelo usuário
    """
    print("\n ------------------- Cadastrando um novo carro -------------------\n")
    car_type = input(
        "Digite o tipo do carro: \n\n - Sedan (1)\n - Hatch (2)\n - SUV (3)\n - Pickup (4)\n - Minivan (5)\n - Esportivo (6)\n\nDigite aqui: "
    )
    
    car_type = get_member_name(int(car_type))
    ports_number = int(input("Digite o número de portas do carro: "))
    power = float(input("Digite a potência do carro: "))
    year = int(input("Digite o ano do carro: "))
    return create_car(car_type, ports_number, power, year)
