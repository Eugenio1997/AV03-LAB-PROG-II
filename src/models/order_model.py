from collections import namedtuple
from datetime import datetime

# Define uma tupla nomeada chamada Car com campos id, tipo, número de portas, potência e ano
Order = namedtuple(
    "Order",
    [
        "id",
        "user_id",
        "status",
        "total_price",
        "total_quantity",
        "created_at",
        "updated_at",
    ],
)


def create_order(
    
) -> Order:
    """
    Retorna um objeto Order com os dados passados como argumentos
    """

    return Order("", "", "", 0.0, 0, datetime.now(), datetime.now())
