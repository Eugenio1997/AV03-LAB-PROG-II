import sqlite3

from prettytable import PrettyTable
from src.enums.car_types import get_member_name
from src.enums.operations import Operation, get_operation_name
from src.models.car_model import Car

def define_table() -> PrettyTable:
    table = PrettyTable()
    table.field_names = ["Id", "Tipo", "Número de Portas", "Potência", "Ano"]
    return table

def confirmation(car_id: int, operation_name: str):
    confirmation = input(f"Tem certeza que deseja {operation_name} o carro com ID {car_id}? (s/n): ")
    if confirmation.lower() == "n":
        print("\n ----- Operação cancelada! -----\n")
        return None
    return True


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
    car_id = input("Digite o ID do carro que deseja visualizar: ")
    car_exists = cursor.execute("SELECT * FROM cars WHERE id = ?", (car_id,)).fetchone()    
    if not car_exists:
        print("\n ----- Carro não encontrado. Por favor, insira um ID válido. -----\n")
        return None
    car_db = Car(id=car_id,type=car_exists[1], ports_number=car_exists[2], power=car_exists[3], year=car_exists[4])
    table = define_table()
    table.add_row([car_id, car_db.type, car_db.ports_number, car_db.power, car_db.year])
    print("\n ------------------- Carro Encontrado -------------------\n")
    print(f"{table}\n")
    

def delete_car_by_id_from_database(cursor: sqlite3.Cursor, conn: sqlite3.Connection):
    car_id = input("Digite o ID do carro que deseja deletar: ")
    
    # Verifica se o carro existe
    car_exists = cursor.execute("SELECT * FROM cars WHERE id = ?", (car_id,)).fetchone()    
    if not car_exists:
        print("\n ----- Carro não encontrado. Por favor, insira um ID válido. -----\n")
        return None
    if (confirmation(car_id, get_operation_name(Operation.DELETAR.value))):
        cursor.execute("DELETE FROM cars WHERE id = ?", (car_id,))
        conn.commit()
        print("\n ----- Carro deletado com sucesso! -----\n")
        return None

def edit_car_by_id_from_database(cursor: sqlite3.Cursor, conn: sqlite3.Connection):
    car_id = input("Digite o ID do carro que deseja editar: ")
    
    # Verifica se o carro existe
    car_exists = cursor.execute("SELECT * FROM cars WHERE id = ?", (car_id,)).fetchone()    
    if not car_exists:
        print("\n ----- Carro não encontrado. Por favor, insira um ID válido. -----\n")
        return None
    if confirmation(car_id, get_operation_name(Operation.EDITAR.value)):
        new_values = get_updated_values(car_id)
        
        update_fields, update_values = making_query_dinamically(new_values)
        
        # Se houver campos para atualizar
        if update_fields:
            update_values.append(car_id)
            update_query = f"UPDATE cars SET {', '.join(update_fields)} WHERE id = ?"
            cursor.execute(update_query, tuple(update_values))
            conn.commit()
            print("\n ----- Carro editado com sucesso! -----\n")
        else:
            print("\n ----- Nenhum campo para atualizar. -----\n")
        
        return None
    
def get_updated_values(car_id: int):
    print(f"\n ------------------- Editando carro de ID {car_id} -------------------\n")
    updated_car_type = input(
        "Digite o tipo do carro: \n\n - Sedan (1)\n - Hatch (2)\n - SUV (3)\n - Pickup (4)\n - Minivan (5)\n - Esportivo (6)\n\nDigite aqui: "
    )
    
    updated_ports_number = input("Digite o número de portas do carro: ")
    updated_power = input("Digite a potência do carro: ")
    updated_year = input("Digite o ano do carro: ")
    return Car(id=car_id, type=updated_car_type, ports_number=updated_ports_number, power=updated_power, year=updated_year)


def making_query_dinamically(new_values: Car):
    update_fields = []
    update_values = []
        
    if new_values.type not in [None, ""]:
        update_fields.append("type = ?")
        update_values.append(get_member_name(int(new_values.type)))
    if new_values.ports_number not in [None, ""]:
        update_fields.append("ports_number = ?")
        update_values.append(int(new_values.ports_number))
    if new_values.power not in [None, ""]:
        update_fields.append("power = ?")
        update_values.append(float(new_values.power))
    if new_values.year not in [None, ""]:
        update_fields.append("year = ?")
        update_values.append(new_values.year)
    
    return update_fields, update_values