from dao.car_dao import edit_car_by_id_from_database


def edit_car_by_id(cursor, conn):
    edit_car_by_id_from_database(cursor, conn)