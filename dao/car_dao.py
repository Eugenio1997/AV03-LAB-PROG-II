import sqlite3

from prettytable import PrettyTable
from src.models.car_model import Car

def define_table() -> PrettyTable:
    table = PrettyTable()
    table.field_names = ["Id", "Tipo", "Número de Portas", "Potência", "Ano"]
    return table

def insert_car_into_database(car: Car, conn: sqlite3.Connection, cursor: sqlite3.Cursor):
    cursor.execute("INSERT INTO cars (type, ports_number, power, year) VALUES (?, ?, ?, ?)", (car.type, car.ports_number, car.power, car.year))
    conn.commit()
    print("\n ----- Carro cadastrado com sucesso! -----\n")

def retrieve_all_cars_from_database(cursor: sqlite3.Cursor):
    cursor.execute("SELECT * FROM cars")
    cars = cursor.fetchall()
    car_objects = [Car(id=car[0] ,type=car[1], ports_number=car[2], power=car[3], year=car[4]) for car in cars]
    table = define_table()
    [table.add_row([car.id ,car.type, car.ports_number, car.power, car.year]) for car in car_objects]
    if not any(table.rows):
        print("\n ----- Nenhum carro encontrado. Por favor, cadastre alguns carros. -----\n")
        return None
    print("\n ------------------- Carros Cadastrados -------------------\n")
    print(f"{table}\n")

def retrieve_car_by_id_from_database(cursor: sqlite3.Cursor):
    option = input("Digite o ID do carro que deseja visualizar: ")
    car_exists = cursor.execute("SELECT * FROM cars WHERE id = ?", (option,)).fetchone()    
    if not car_exists:
        print("\n ----- Carro não encontrado. Por favor, insira um ID válido. -----\n")
        return None
    car_db = Car(type=car_exists[1], ports_number=car_exists[2], power=car_exists[3], year=car_exists[4])
    table = define_table()
    table.add_row([car_db.type, car_db.ports_number, car_db.power, car_db.year])
    print("\n ------------------- Carro Encontrado -------------------\n")
    print(f"{table}\n")
    

def delete_car_by_id_from_database(cursor: sqlite3.Cursor, conn: sqlite3.Connection):
    car_id = input("Digite o ID do carro que deseja deletar: ")
    
    # Verifica se o carro existe
    car_exists = cursor.execute("SELECT * FROM cars WHERE id = ?", (car_id,)).fetchone()    
    if not car_exists:
        print("\n ----- Carro não encontrado. Por favor, insira um ID válido. -----\n")
        return None
    if (delete_confirmation(car_id)):
        cursor.execute("DELETE FROM cars WHERE id = ?", (car_id,))
        conn.commit()
        print("\n ----- Carro deletado com sucesso! -----\n")
        return None

def delete_confirmation(car_id: int):
    confirmation = input(f"Tem certeza que deseja deletar o carro com ID {car_id}? (s/n): ")
    if confirmation.lower() == "n":
        print("\n ----- Carro não deletado. -----\n")
        return None
    return True