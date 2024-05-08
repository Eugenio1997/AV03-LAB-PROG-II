import sqlite3

counter = 0
def create_connection():
    """
        Abre uma conexão de banco de dados com a base de dados Carfolio 
    """
    global counter
    
    if counter == 0:
        try:
            _conn = sqlite3.connect('Carfolio.db')
            print("\nConexão com o banco de dados estabelecida com sucesso!")
            counter += 1
        except sqlite3.Error as e:
            print(e)
    return _conn

def open_connection():
    """
        Abre uma conexão de banco de dados e retorna a conexão e o cursor
    """
    conn = create_connection()
    cursor = conn.cursor()
    return conn, cursor
    
def close_connection(conn):  # Pass connection and cursor as parameters
    if conn:
        conn.close()
