from faker import Faker
from src.enums.car_types import CarType



def seeder(conn, cursor):
    """
        Funcão para popular o banco de dados com dados falsos
    """
    is_seeded(conn, cursor)


# Faker instance for generating fake data
fake = Faker()

# Create cars table
create_cars_table_query = """
CREATE TABLE IF NOT EXISTS cars (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    type TEXT NOT NULL,
    ports_number TEXT NOT NULL,
    power FLOAT NOT NULL,
    year INT NOT NULL,
    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
);
"""

# Create configuration table
create_configuration_table_query = """
CREATE TABLE IF NOT EXISTS configuration (
    seeded INTEGER CHECK (seeded IN (0, 1))  
);
"""    
    
def create_tables(cursor):
    cursor.execute(create_cars_table_query)
    cursor.execute(create_configuration_table_query)


# Seed users table
def populate_cars_table(cursor):
    for _ in range(10):
        car_type = fake.random.choice(list(CarType))  # Get a random car type from the enum
        ports_number = fake.random_int(2, 4, 2)  # Example range for number of ports
        power = fake.random_int(90, 1000)  # Example range for power
        year = fake.year()  # Get a fake year
        car_data = (car_type.name, ports_number, power, year)  # Pack data into a tuple
        cursor.execute("INSERT INTO cars (type, ports_number, power, year) VALUES (?, ?, ?, ?)", car_data)


# Seed configuration table       
def populate_configuration_table(cursor):
    cursor.execute("INSERT INTO configuration (seeded) VALUES (0)")


def create_and_populate_all_tables(cursor) -> None:
    create_tables(cursor)
    populate_cars_table(cursor)
    populate_configuration_table(cursor)
    
def apply_migrations_and_mark_seeded_on_config_table(conn, cursor) -> None:
    create_and_populate_all_tables(cursor)
    mark_seeded(conn, cursor)
    conn.commit()
        
def is_seeded(conn, cursor):

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

def mark_seeded(conn, cursor):
    # Define a flag seeded na base de dados
    cursor.execute("UPDATE configuration SET seeded = 1")
    

