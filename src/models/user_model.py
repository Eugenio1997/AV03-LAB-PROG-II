from collections import namedtuple


# Define uma tupla nomeada chamada User com campos id, nome, email e senha
User = namedtuple('user', ['id','name', 'email', 'password'])

def create_user(name: str, email: str, password: str) -> User:
    """
        Retorna um objeto User com os dados passados como argumentos
    """

    return User(id, name, email, password)
