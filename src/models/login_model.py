from collections import namedtuple


# Define uma tupla nomeada chamada User_Login com campos email e senha
User_Login = namedtuple('user_login', ['email', 'password'])

def create_user_login(email: str, password: str) -> User_Login:
    """
        Retorna um objeto User_Login com os dados passados como argumentos
    """

    return User_Login(email, password)
