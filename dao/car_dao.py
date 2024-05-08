import sqlite3

from prettytable import PrettyTable
from src.models.car_model import Car


def insert_car_into_database(car: Car, conn: sqlite3.Connection, cursor: sqlite3.Cursor):
    cursor.execute("INSERT INTO cars (type, ports_number, power, year) VALUES (?, ?, ?, ?)", (car.type, car.ports_number, car.power, car.year))
    conn.commit()
    print("\n ----- Carro cadastrado com sucesso! -----\n")

def retrieve_all_cars_from_database(conn, cursor):
    table: PrettyTable = PrettyTable()
    table.field_names = ["Tipo", "Número de Portas", "Potência", "Ano"]
    cursor.execute("SELECT * FROM cars")
    cars = cursor.fetchall()
    car_objects = [Car(type=car[1], ports_number=car[2], power=car[3], year=car[4]) for car in cars]
    [table.add_row([car.type, car.ports_number, car.power, car.year]) for car in car_objects]
    if not any(table.rows):
        print("\n ----- Nenhum carro encontrado. Por favor, cadastre alguns carros. -----\n")
        return None
    print("\n ------------------- Carros Cadastrados -------------------\n")
    print(f"{table}\n")
    