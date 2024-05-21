

from dao.car_dao import delete_car_by_id_from_database


def delete_car_by_id(cursor, conn):
    delete_car_by_id_from_database(cursor, conn)