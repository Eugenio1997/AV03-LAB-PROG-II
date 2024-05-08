

from dao.car_dao import retrieve_all_cars_from_database


def display_all_cars(conn, cursor) -> None:
    """"
        Recupera todos os carros da database e os exibe
        no formato tabular.
    """
    retrieve_all_cars_from_database(conn, cursor)

    