from collections import namedtuple
from src.enums.car_types import CarType


# Define uma tupla nomeada chamada Car com campos tipo, número de portas, potência e ano
Car = namedtuple('car', ['type', 'ports_number', 'power', 'year',])

def create_car(car_type: CarType, ports_number: int, power: float, year: int) -> Car:
    """
        Retorna um objeto Car com os dados passados como argumentos
    """
    return Car(car_type, ports_number, power, year)
