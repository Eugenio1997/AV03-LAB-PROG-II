# src/orders/operations.py

from datetime import datetime

from prettytable import PrettyTable
from dao.order_dao import create_new_order_on_orders_table
from src.enums.order_status import Order_Status
from src.models.order_model import Order
from src.models.line_item_model import create_line_item
from src.enums.shopping_cart_menu import Shopping_Cart_Menu
from src.interface.user_interface import show_shopping_cart_menu
from src.user.login import get_authenticated_user_email

# Define a global list to store items
items = []


def define_line_item_table_header() -> PrettyTable:
    table = PrettyTable()
    table.field_names = [
        "Pedido ID",
        "Carro ID",
        "Quantidade",
        "Preço",
        "Criado em",
        "Atualizado em",
    ]
    return table

def define_order_table_header() -> PrettyTable:
    table = PrettyTable()
    table.field_names = [
        "Pedido ID",
        "Usuário ID",
        "Status",
        "Preço Total",
        "Quantidade Total",
        "Criado em",
        "Atualizado em",
    ]
    return table



def add_item_to_cart(conn, cursor):
        
    option = show_shopping_cart_menu()
    
    if check_if_latest_finished_purchase(cursor) and option not in [
            Shopping_Cart_Menu.VIEW_CONFIRMED_ORDERS.value,
            Shopping_Cart_Menu.DISPLAY_CART.value,
            Shopping_Cart_Menu.ADD_ITEM.value,
        ]:
        order_id = create_new_order_on_orders_table(conn, cursor)
    else:
        order_id = cursor.execute("SELECT id FROM orders ORDER BY id DESC LIMIT 1").fetchone()[0]

    if option == Shopping_Cart_Menu.ADD_ITEM.value:
        print("\n ------ Adicionando um carro ao carrinho de compras ------\n")

        car_id = int(input("\nDigite o ID do carro: "))
        carDb = cursor.execute("SELECT * FROM cars WHERE id = ?", (car_id,)).fetchone()
        quantity = int(input("Digite a quantidade: "))
        
        # Flag to check if the car is already in the cart
        car_found = False

        # Check if the car_id already exists in the cart
        for item in items:
            if item['car_id'] == car_id:
                item['quantity'] = quantity
                item['price'] = carDb[4] * item['quantity']
                item['updated_at'] = datetime.now()
                print("\n ------ Quantidade atualizada ------")
                car_found = True
                break
        
        if not car_found:
            
            items.append(
                create_line_item(
                    order_id=order_id,
                    car_id=car_id,
                    quantity=quantity,
                    price=carDb[4] * quantity,
                    created_at=datetime.now(),
                    updated_at=datetime.now(),
                )
            )
            print("\n ------ Carro adicionado ao carrinho ------")
            
        return True



    elif option == Shopping_Cart_Menu.REMOVE_ITEM.value:
        car_id = int(input("Digite o ID do carro que deseja remover: "))
        for item in items:
            if item["car_id"] == car_id:
                items.remove(item)
                print("\n ------ Carro removido do carrinho ------")
                break
        if not any(items):
            print("\n ----- Sacola vazia. Por favor, adicione items à sacola. -----\n")
        return True
    elif option == Shopping_Cart_Menu.DISPLAY_CART.value:
        line_item_objects = [
            create_line_item(
                order_id=line_item['order_id'],
                car_id=line_item['car_id'],
                quantity=line_item['quantity'],
                price=line_item['price'],
                created_at=line_item['created_at'],
                updated_at=line_item['updated_at'],
            )
            for line_item in items
        ]

        table = define_line_item_table_header()
        [
            table.add_row(
                [
                    line_item['order_id'],
                    line_item['car_id'],
                    line_item['quantity'],
                    line_item['price'],
                    line_item['created_at'],
                    line_item['updated_at'],
                ]
            )
            for line_item in line_item_objects
        ]
        if len(line_item_objects) == 0:
            print("\n ----- Sacola vazia. Por favor, adicione items à sacola. -----\n")
        else:
            print("\n ------------------- Carrinho de Compras -------------------\n")
            print(f"{table}\n")
        return True


    elif option == Shopping_Cart_Menu.VIEW_CONFIRMED_ORDERS.value:
        logged_in_user = get_logged_in_user(cursor)
        logged_in_user_orders = cursor.execute(
            "SELECT * FROM orders WHERE user_id = ? AND status = ?",
            (logged_in_user[0], Order_Status.CONFIRMED.value),
        ).fetchall()
        if logged_in_user_orders:
            order_objects = [
                Order(
                    id=order[0],
                    user_id=order[1],
                    total_price=order[2],
                    total_quantity=order[3],
                    created_at=order[4],
                    updated_at=order[5],
                )
                for order in logged_in_user_orders
            ]

            table = define_line_item_table_header()
            [
                table.add_row(
                    [
                        order.id,
                        order.user_id,
                        order.total_price,
                        order.total_quantity,
                        order.created_at,
                        order.updated_at,
                    ]
                )
                for order in order_objects
            ]
            print("\n ------------------- Pedidos Confirmados -------------------\n")
            print(f"{table}\n")
        else:
            print("\n ----- Nenhum pedido confirmado encontrado. -----\n")
        return True


    elif option == Shopping_Cart_Menu.FINISH_PURCHASE.value:
        insert_line_items_into_database(cursor, conn)
        return insert_order_into_database(cursor, conn, order_id)
    
    elif option == Shopping_Cart_Menu.RETRIEVE_LAST_ORDER.value:
        return retrive_last_order(cursor)

    elif option == Shopping_Cart_Menu.CANCEL_PURCHASE.value:
        items.clear()  # Limpa a lista de items
        print("\n ----- Compra cancelada com sucesso! -----\n")
        print("\n ----- Sacola vazia. Por favor, adicione items à sacola. -----\n")
        return True
    elif option == Shopping_Cart_Menu.BACK_TO_MAIN_MENU.value:
        return False
    else:
        print("Opção inválida")


def make_order(conn, cursor):
    while True:
        should_continue = add_item_to_cart(conn, cursor)
        if not should_continue:
            return False


def delete_current_order(conn, cursor, order_id):
    cursor.execute("DELETE FROM orders WHERE id = ?", (order_id,))
    conn.commit()
    print("Pedido cancelado com sucesso!")
    return True


def check_if_latest_finished_purchase(cursor):
    last_order_id_result = cursor.execute(
        "SELECT id FROM orders WHERE status = ? ORDER BY id DESC LIMIT 1",
        (Order_Status.CONFIRMED.value,),
    ).fetchone()
    if last_order_id_result:
        last_order_id = last_order_id_result[0]
        return True
    return False


def get_logged_in_user(cursor):
    logged_in_user_email = get_authenticated_user_email()
    logged_in_user = cursor.execute(
        "SELECT * FROM users WHERE email = ?", (logged_in_user_email,)
    ).fetchone() 
    return logged_in_user

def insert_line_items_into_database(cursor, conn):
    
    if not items:
        return True
   
    for item in items:
        cursor.execute(
            "INSERT INTO line_items (order_id, car_id, quantity, price, created_at, updated_at) VALUES (?, ?, ?, ?, ?, ?)",
            (
                item["order_id"],
                item["car_id"],
                item["quantity"],
                item["price"],
                item["created_at"],
                item["updated_at"],
            ),
        )
    conn.commit()


def insert_order_into_database(cursor, conn, order_id):
    logged_in_user = get_logged_in_user(cursor)
    
    if not items:
        print("\n ----- Nenhum item no carrinho. Por favor, adicione items ao carrinho. -----\n")
        return True
    try:
        status = Order_Status.CONFIRMED.value
        total_price = sum(item["price"] for item in items)
        total_quantity = sum(item["quantity"] for item in items)
        
        cursor.execute(
            "UPDATE orders SET status = ?, total_price = ?, total_quantity = ? WHERE id = ?",
            (status, total_price, total_quantity, order_id),
        )
        conn.commit()
        print("\n ----- Pedido finalizado com sucesso! -----\n")
        print(f"\n ----- Obrigado por comprar conosco {logged_in_user[1]}! -----\n")
        items.clear()
        return True
    except Exception as e:
        print(f"Erro ao finalizar o pedido: {e}")
        return False
   

def retrive_last_order(cursor):
    logged_in_user = get_logged_in_user(cursor)
    cursor.execute(
        "SELECT id, user_id, status, total_price, total_quantity, created_at, updated_at FROM orders WHERE user_id = ? AND status = ? ORDER BY id DESC LIMIT 1",
        (logged_in_user[0], Order_Status.CONFIRMED.value),
    )
    last_confirmed_order = cursor.fetchone()
    if last_confirmed_order:
        table = define_order_table_header()
        table.add_row(last_confirmed_order)
        print(table)
    else:
        print("\n ----- Nenhum pedido confirmado encontrado para este usuário. -----\n")

    return True
