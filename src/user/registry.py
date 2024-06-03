## What function name would be good to registry a new user?

import sqlite3

import bcrypt

from dao.user_dao import insert_new_user_into_database
from src.models.user_model import User, create_user


def register_user(conn: sqlite3.Connection, cursor: sqlite3.Cursor) -> None:
    """ "
    Realiza o cadastro do usuario na database
    """
    new_user = get_user_data()
    insert_new_user_into_database(new_user, conn, cursor)


def get_user_data() -> User:
    """
    Retorna um objeto User com os dados inseridos pelo usuário
    """
    print("\n ------------------- Cadastrando um novo usuario -------------------\n")
    name = input("Digite o nome do usuario: ")
    email = input("Digite o email do usuario: ")
    password = input("Digite a senha do usuario: ")
    
    salt = bcrypt.gensalt(rounds=12, prefix=b"2b")
    password = bcrypt.hashpw(password.encode('utf-8'), salt).decode('utf-8')  # Hash the password
    return create_user(name, email, password)
