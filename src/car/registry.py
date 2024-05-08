from enums.car_types import CarType
from collections import namedtuple

# Defina uma tupla nomeada chamada Car com campos tipo, número de portas, potência e ano
Car = namedtuple('car', ['type', 'ports_number', 'power', 'year',])

def register_car(type: CarType, ports_number: int, power: float, year: int):
    """"
        Realiza o cadastro do carro na database    
    """
    pass