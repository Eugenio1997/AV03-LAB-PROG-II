import sqlite3
from faker import Faker
from src.enums.car_types import CarType
import bcrypt



def seeder(conn: sqlite3.Connection, cursor: sqlite3.Cursor):
    """
        Funcão para popular o banco de dados com dados falsos
    """
    is_seeded(conn, cursor)


# Faker instance for generating fake data
fake = Faker()

#Create users table
create_users_table_query = """
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL,
    password TEXT NOT NULL,
    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(email)
);
"""

# Create cars table
create_cars_table_query = """
CREATE TABLE IF NOT EXISTS cars (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    type TEXT NOT NULL,
    ports_number TEXT NOT NULL,
    power FLOAT NOT NULL,
    price FLOAT NOT NULL,
    year INT NOT NULL,
    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
);
"""

#Create orders table
create_orders_table_query = """
CREATE TABLE IF NOT EXISTS orders (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL REFERENCES users(id) ON DELETE CASCADE ON UPDATE CASCADE,
    status TEXT NOT NULL DEFAULT 'pending',
    total_price FLOAT NOT NULL,
    total_quantity INTEGER NOT NULL,
    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id)
);
"""

#Create line_items table
create_line_items_table_query = """
CREATE TABLE IF NOT EXISTS line_items (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    order_id INTEGER NOT NULL REFERENCES orders(id) ON DELETE CASCADE ON UPDATE CASCADE,
    car_id INTEGER NOT NULL REFERENCES cars(id) ON DELETE CASCADE ON UPDATE CASCADE,
    quantity INTEGER NOT NULL,
    price FLOAT NOT NULL,
    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (order_id) REFERENCES orders(id),
    FOREIGN KEY (car_id) REFERENCES cars(id)
);
"""

# Create configuration table
create_configuration_table_query = """
CREATE TABLE IF NOT EXISTS configuration (
    seeded INTEGER CHECK (seeded IN (0, 1))  
);
"""    
    
def create_tables(cursor):
    cursor.execute(create_users_table_query)
    cursor.execute(create_cars_table_query)
    cursor.execute(create_orders_table_query)
    cursor.execute(create_line_items_table_query) 
    cursor.execute(create_configuration_table_query)
  

salt = bcrypt.gensalt(rounds=12, prefix=b"2b")


def populate_users_table(cursor):
    #Seed Admin user
    name = 'admin123'
    email = "admin@123.com"
    password = bcrypt.hashpw("123456".encode("utf-8"), salt).decode(
        "utf-8"
    )  # Hash the password
    created_at = "2021-01-01 00:00:00"
    updated_at = "2021-01-01 00:00:00"
    user_data = (name, email, password, created_at, updated_at)
    cursor.execute(
        "INSERT INTO users (name, email, password, created_at, updated_at) VALUES (?, ?, ?, ?, ?)",
        user_data,
    )
    #Seed 10 users
    for _ in range(10):
        name = fake.name()
        email = fake.email()
        password = bcrypt.hashpw("123456".encode('utf-8'), salt).decode('utf-8')  # Hash the password
        created_at = fake.date_time_this_year()  # Get a fake date
        updated_at = fake.date_time_this_year()  # Get a fake date
        user_data = (name, email, password, created_at, updated_at)
        cursor.execute("INSERT INTO users (name, email, password, created_at, updated_at) VALUES (?, ?, ?, ?, ?)", user_data)

# Seed users table
def populate_cars_table(cursor):
    for _ in range(10):
        car_type = fake.random.choice(list(CarType))  # Get a random car type from the enum
        ports_number = fake.random_int(2, 4, 2)  # Example range for number of ports
        power = fake.random_int(90, 1000)  # Example range for power
        price = fake.random_int(10000, 100000)  # Example range for price
        year = fake.year()  # Get a fake year
        created_at = fake.date_time_this_year()  # Get a fake date
        updated_at = fake.date_time_this_year()  # Get a fake date
        car_data = (car_type.name, ports_number, power, price, year, created_at, updated_at)  # Pack data into a tuple
        cursor.execute("INSERT INTO cars (type, ports_number, power, price, year, created_at, updated_at) VALUES (?, ?, ?, ?, ?, ?, ?)", car_data)

def populate_orders_table(cursor):
    for _ in range(10):
        user_id = fake.random_int(1, 10)  # Get a random user id
        status = fake.random.choice(["pending", "completed", "cancelled"])  # Get a random status
        created_at = fake.date_time_this_year()  # Get a fake date
        updated_at = fake.date_time_this_year()  # Get a fake date

        # Insert the order into the orders table
        cursor.execute(
            "INSERT INTO orders (user_id, status, total_price, total_quantity, created_at, updated_at) VALUES (?, ?, ?, ?, ?, ?)",
            (user_id, status, 0, 0, created_at, updated_at),
        )

        # Retrieve the order_id of the newly inserted order
        order_id = cursor.lastrowid

        # Calculate the total price of the order
        cursor.execute(
            "SELECT IFNULL(SUM(price), 0) FROM line_items WHERE order_id = ?",
            (order_id,),
        )
        total_price = cursor.fetchone()[0]

        # Update the total price in the orders table
        cursor.execute(
            "UPDATE orders SET total_price = ? WHERE id = ?", (total_price, order_id)
        )

        # Calculate the total quantity in the orders table
        cursor.execute(
            "SELECT IFNULL(SUM(quantity), 0) FROM line_items WHERE order_id = ?",
            (order_id,),
        )
        total_quantity = cursor.fetchone()[0]

        # Update the total quantity in the orders table
        cursor.execute(
            "UPDATE orders SET total_quantity = ? WHERE id = ?",
            (total_quantity, order_id),
        )


def populate_line_items_table(cursor):
    for _ in range(10):
        order_id = fake.random_int(1, 10)  # Get a random order id
        car_id = fake.random_int(1, 10)  # Get a random car id
        quantity = fake.random_int(1, 10)  # Get a random quantity
        # Fetch the price from the database
        cursor.execute("SELECT price FROM cars WHERE id = ?", (car_id,))
        result = cursor.fetchone()
        if result:
            car_price = result[0]  # Unpack the tuple to get the price value
            price = car_price * quantity  # Calculate the total price
            created_at = fake.date_time_this_year()  # Get a fake date
            updated_at = fake.date_time_this_year()  # Get a fake date
            line_item_data = (order_id, car_id, quantity, price, created_at, updated_at)
            cursor.execute(
                "INSERT INTO line_items (order_id, car_id, quantity, price, created_at, updated_at) VALUES (?, ?, ?, ?, ?, ?)",
                line_item_data,
            )


# Seed configuration table       
def populate_configuration_table(cursor):
    cursor.execute("INSERT INTO configuration (seeded) VALUES (0)")

def create_and_populate_all_tables(cursor) -> None:
    create_tables(cursor)
    populate_users_table(cursor)
    populate_cars_table(cursor)
    populate_orders_table(cursor)
    populate_line_items_table(cursor)
    populate_configuration_table(cursor)
    
def apply_migrations_and_mark_seeded_on_config_table(conn, cursor) -> None:
    create_and_populate_all_tables(cursor)
    mark_seeded(cursor)
    conn.commit()
        
def is_seeded(conn: sqlite3.Connection, cursor: sqlite3.Cursor):

    try: ## vai ser executado a partir da segunda vez que o programa for executado
        # Verifica se a flag seeded está definida na base de dados
        cursor.execute("SELECT seeded FROM configuration")
        result = cursor.fetchone()
        if result and result[0] == 1:
            return True
        apply_migrations_and_mark_seeded_on_config_table(conn, cursor)
    except Exception as e: ##vai ser executado na primeira vez que o programa for executado
        apply_migrations_and_mark_seeded_on_config_table(conn, cursor)
        return False

def mark_seeded(cursor: sqlite3.Cursor):
    # Define a flag seeded na base de dados
    cursor.execute("UPDATE configuration SET seeded = 1")
    

