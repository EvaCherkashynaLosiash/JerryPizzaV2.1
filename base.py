import sqlite3


def init_db():
    with sqlite3.connect("pizza_database.db") as connection:
        connection.executescript("""
        CREATE TABLE IF NOT EXISTS pizzas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            description TEXT NOT NULL,
            price REAL NOT NULL
        );
        """)
    print("✅ bаза данных и таблица ")


def get_db_connection():
    connection = sqlite3.connect("pizza_database.db")
    connection.row_factory = sqlite3.Row
    return connection


def data():
    pizzas = [
        {"name": "Мишачий Класик", "description": "Сир, томати, базилік", "price": 150},
        {"name": "Пепероні від Тома", "description": "пепероні, шинка, ковбаски, соус барбекю", "price": 180},
        {"name": "Джеррі в Сирі", "description": "Моцарела, горгонзола, пармезан, чеддер", "price": 200},
        {"name": "Сирний Джеррі", "description": "моцарела, чеддер, пармезан, рікотта, любов", "price": 250},
        {"name": "Томовий Барбекю", "description": "курка, бекон, соус барбекю, червоний лук", "price": 300},
    ]

    connection = get_db_connection()
    cursor = connection.cursor()

    for pizza in pizzas:
        cursor.execute(
            "INSERT INTO pizzas (name, description, price) VALUES (?, ?, ?)",
            (pizza["name"], pizza["description"], pizza["price"])
        )

    connection.commit()
    connection.close()

    print("✅ данные ")