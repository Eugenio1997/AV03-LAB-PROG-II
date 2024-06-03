import sqlite3
import bcrypt
from prettytable import PrettyTable

from src.models.user_model import User


def define_table() -> PrettyTable:
    table = PrettyTable()
    table.field_names = ['id','name', 'email', 'password']
    return table

def insert_new_user_into_database(user: User, conn: sqlite3.Connection, cursor: sqlite3.Cursor):
    cursor.execute("INSERT INTO users (name, email, password) VALUES (?, ?, ?)", (user.name, user.email, user.password))
    conn.commit()
    print("\n ----- Usuario cadastrado com sucesso! -----\n")

def check_if_user_exists(user_login_data, cursor):
    
    cursor.execute("SELECT * FROM users WHERE email = ?", (user_login_data.email,))
    user = cursor.fetchone()
    if not user:
        print("\n ----- Usuario não encontrado. Por favor, insira um email válido. -----\n")
        return False
    if bcrypt.checkpw(user_login_data.password.encode('utf-8'), user[3].encode('utf-8')):
        print("\n ----- Usuario logado com sucesso! -----\n")
        return True
    else:
        print("\n ----- Senha incorreta. Por favor, insira uma senha válida. -----\n")
        return False


def retrieve_all_users_from_database(cursor: sqlite3.Cursor):
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    user_objects = [User(id=user[0] ,name=user[1], email=user[2], password=user[3]) for user in users]
    table = define_table()
    [table.add_row([user.id ,user.name, user.email, user.password]) for user in user_objects]
    if not any(table.rows):
        print("\n ----- Nenhum usuario encontrado. Por favor, cadastre alguns usuarios. -----\n")
        return None
    print("\n ------------------- Usuarios Cadastrados -------------------\n")
    print(f"{table}\n")