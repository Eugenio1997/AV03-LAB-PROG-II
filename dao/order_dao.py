from datetime import datetime
from src.enums.order_status import Order_Status
from src.user.login import get_authenticated_user_email


def create_new_order_on_orders_table(conn, cursor, is_make_order=True):
    # Assuming get_authenticated_user_email() is a function that returns the authenticated user's email
    authenticated_user_email = get_authenticated_user_email()

    # Fetch the user ID from the database based on the authenticated user's email
    cursor.execute("SELECT id FROM users WHERE email = ?", (authenticated_user_email,))
    user_id = cursor.fetchone()
    if user_id is not None and is_make_order is True:
        cursor.execute(
            "INSERT INTO orders (user_id, status, total_price, total_quantity, created_at, updated_at) VALUES (?, ?, ?, ?, ?, ?)",
            (user_id[0], Order_Status.PENDING.value, 0, 0, datetime.now(), datetime.now()),
        )
        order_id = cursor.lastrowid
        conn.commit()
        print("\n ----- Pedido finalizado encontrado. Criando um novo pedido. -----\n")
        return order_id
    else:
        # Handle the case where the user does not exist
        raise ValueError("User does not exist")