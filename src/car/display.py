

from dao.car_dao import retrieve_all_cars_from_database, retrieve_car_by_id_from_database


def display_all_cars(conn, cursor) -> None:
    """"
        Recupera todos os carros da database e os exibe
        no formato tabular.
    """
    retrieve_all_cars_from_database(cursor)

def display_car_by_id(conn, cursor) -> None:
    retrieve_car_by_id_from_database(cursor)