import sqlite3

connection = sqlite3.connect("bd_test.db")
cursor = connection.cursor()


def display_stores():
    cursor.execute("SELECT store_id, title FROM store")
    stores = cursor.fetchall()

    print(
        "Вы можете отобразить список продуктов по выбранному id магазина из перечня магазинов ниже, для выхода из программы введите цифру 0:")
    for store in stores:
        print(f"{store[0]}. {store[1]}")


def display_products_by_store(store_id):
    query = """
    SELECT p.title, c.title, p.unit_price, p.stock_quantity
    FROM products p
    JOIN categories c ON p.category_code = c.code
    WHERE p.store_id = ?
    """
    cursor.execute(query, (store_id,))
    products = cursor.fetchall()

    if products:
        for product in products:
            print(f"Название продукта: {product[0]}")
            print(f"Категория: {product[1]}")
            print(f"Цена: {product[2]}")
            print(f"Количество на складе: {product[3]}\n")
    else:
        print("Продукты для выбранного магазина не найдены.")


def main():
    while True:
        display_stores()
        try:
            store_id = int(input("Введите id магазина: "))
            if store_id == 0:
                break
            display_products_by_store(store_id)
        except ValueError:
            print("Пожалуйста, введите корректный номер магазина.")

    print("Выход из программы.")
    connection.close()


if __name__ == "__main__":
    main()
