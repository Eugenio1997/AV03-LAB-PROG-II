from datetime import datetime


def create_line_item(
    order_id: int,
    car_id: int,
    quantity: int,
    price: float,
    created_at: datetime,
    updated_at: datetime,
) -> dict:
    """
    Retorna um dicionário representando um item de linha com os dados passados como argumentos
    """
    return {
        "order_id": order_id,
        "car_id": car_id,
        "quantity": quantity,
        "price": price,
        "created_at": created_at,
        "updated_at": updated_at,
    }
