import sqlite3
from dao.user_dao import check_if_user_exists
from src.models.login_model import User_Login, create_user_login

is_user_authenticated = False  # Variável global para armazenar o estado de autenticação
authenticated_user_email = ''  # Variável global para armazenar o nome do usuário autenticado

def authenticate_user(conn: sqlite3.Connection, cursor: sqlite3.Cursor) -> None:
    """
    Realiza o login do usuário na database
    """
    global is_user_authenticated  # Declara a variável global dentro da função
    user_login_data = get_user_login_data()
    is_user_authenticated = check_if_user_exists(user_login_data, cursor)

def get_user_login_data() -> User_Login:
    """
    Retorna um objeto User_Login com os dados inseridos pelo usuário
    """
    print(
        "\n\n\nCaso deseje ter privilégios de administrador como:\n\n"
        "- Deletar carro por ID\n"
        "- Editar carro por ID\n"
        "- Registrar novo carro\n"
        "- Visualizar carro por ID\n"
        "- Visualizar todos os carros\n\n"
        "---> Digite o email: admin@123.com\n"
        "---> Digite a senha: 123456\n\n\n"
    )
    print("\n ------------------- Realizando a autenticação do usuário -------------------\n")
    email = input("Digite o email: ")
    password = input("Digite a senha: ")
    global authenticated_user_email  # Declara a variável global dentro da função
    authenticated_user_email = email
    
    return create_user_login(email, password)

def get_authentication_status() -> bool:
    """
    Retorna o estado de autenticação do usuário
    """
    global is_user_authenticated  # Declara a variável global dentro da função
    return is_user_authenticated

def logout():
    """
    Realiza o logout do usuário
    """
    global is_user_authenticated  # Declara a variável global dentro da função
    global authenticated_user_email  # Declara a variável global dentro da função
    is_user_authenticated = False
    authenticated_user_email = ''
    print("\n ----- Usuário deslogado com sucesso! -----\n")

def get_authenticated_user_email() -> str:
    """
    Retorna o email do usuário autenticado
    """
    global authenticated_user_email  # Declara a variável global dentro da função
    return authenticated_user_email