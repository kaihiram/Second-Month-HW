import sqlite3

# Создание базы данных и подключение к ней
def create_database():
    conn = sqlite3.connect('hw.db')
    cursor = conn.cursor()

    # Создание таблицы products с уникальным полем product_title
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            product_title TEXT NOT NULL CHECK(length(product_title) <= 200),
            price REAL NOT NULL DEFAULT 0.0 CHECK(price >= 0.0),
            quantity INTEGER NOT NULL DEFAULT 0,
            UNIQUE(product_title)
        )
    ''')
    conn.commit()
    conn.close()

def add_products():
    conn = sqlite3.connect('hw.db')
    cursor = conn.cursor()

    products = [
        ('Мыло', 10.99, 50),
        ('Детское мыло', 15.75, 20),
        ('Шампунь для волос', 5.49, 100),
        ('Гель для душа', 7.25, 30),
        ('Зубная паста', 3.99, 200),
        ('Крем для лица', 9.99, 75),
        ('Лосьон для тела', 12.49, 60),
        ('Бальзам для губ', 8.99, 90),
        ('Маска для волос', 14.99, 10),
        ('Скраб для тела', 6.50, 150),
        ('Туалетная бумага', 11.49, 40),
        ('Мочалка для тела', 13.99, 80),
        ('Крем для рук', 4.99, 110),
        ('Дезодорант', 5.75, 250),
        ('Пена для бритья', 10.25, 55)
    ]

    # Используем INSERT OR IGNORE для предотвращения дубликатов
    cursor.executemany('''
        INSERT OR IGNORE INTO products (product_title, price, quantity)
        VALUES (?, ?, ?)
    ''', products)

    conn.commit()
    conn.close()

    print("Товары добавлены (дубликаты пропущены).")


# Функция для изменения количества товара по id
def update_quantity(product_id, new_quantity):
    conn = sqlite3.connect('hw.db')
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE products SET quantity = ? WHERE id = ?
    ''', (new_quantity, product_id))

    conn.commit()
    conn.close()

# Функция для изменения цены товара по id
def update_price(product_id, new_price):
    conn = sqlite3.connect('hw.db')
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE products SET price = ? WHERE id = ?
    ''', (new_price, product_id))

    conn.commit()
    conn.close()

# Функция для удаления товара по id
def delete_product(product_id):
    conn = sqlite3.connect('hw.db')
    cursor = conn.cursor()
    cursor.execute('''
        DELETE FROM products WHERE id = ?
    ''', (product_id,))

    conn.commit()
    conn.close()

# Функция для вывода всех товаров
def fetch_all_products():
    conn = sqlite3.connect('hw.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM products')
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    conn.close()

# Функция для выборки товаров дешевле лимита по цене и количеством больше лимита
def fetch_products_under_price_and_quantity(price_limit, quantity_limit):
    conn = sqlite3.connect('hw.db')
    cursor = conn.cursor()
    cursor.execute('''
        SELECT * FROM products
        WHERE price < ? AND quantity > ?
    ''', (price_limit, quantity_limit))

    rows = cursor.fetchall()
    for row in rows:
        print(row)

    conn.close()

# Функция для поиска товаров по названию
def search_product_by_name(search_term):
    conn = sqlite3.connect('hw.db')
    cursor = conn.cursor()
    cursor.execute('''
        SELECT * FROM products
        WHERE LOWER(product_title) LIKE LOWER(?)
    ''', ('%' + search_term + '%',))

    rows = cursor.fetchall()
    for row in rows:
        print(row)

    conn.close()



if __name__ == '__main__':
    create_database()
    add_products()

    print("Все товары:")
    fetch_all_products()

    print("\nОбновляем количество товара с id 1:")
    update_quantity(1, 700)
    fetch_all_products()

    print("\nОбновляем цену товара с id 2:")
    update_price(2, 19.99)
    fetch_all_products()

    print("\nУдаляем товар с id 3:")
    delete_product(3)
    fetch_all_products()

    print("\nТовары дешевле 100 сом и количество больше 5 шт:")
    fetch_products_under_price_and_quantity(100, 5)

    print("\nПоиск товаров по слову 'мыло':")
    search_product_by_name('мыло')
