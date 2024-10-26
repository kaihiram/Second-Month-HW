import sqlite3


def get_cities(cursor):
    cursor.execute("SELECT id, title FROM cities")
    return cursor.fetchall()


def get_students_by_city_id(cursor, city_id):
    query = """
    SELECT s.first_name, s.last_name, c.title AS city, c.area, ct.title AS country
    FROM students s
    JOIN cities c ON s.city_id = c.id
    JOIN countries ct ON c.country_id = ct.id
    WHERE c.id = ?
    """
    cursor.execute(query, (city_id,))
    return cursor.fetchall()


def main():
    conn = sqlite3.connect('hw_8.db')
    cursor = conn.cursor()

    print(
        "Вы можете отобразить список учеников по выбранному id города из перечня городов ниже, для выхода из программы введите 0:")

    cities = get_cities(cursor)
    for i, city in enumerate(cities, start=1):
        print(f"{i}. {city[1]}")

    while True:
        try:
            city_id = int(input("\nВведите id города: "))
            if city_id == 0:
                print("Выход из программы.")
                break

            students = get_students_by_city_id(cursor, city_id)
            if students:
                print(f"\nСписок учеников, проживающих в выбранном городе (ID: {city_id}):")
                for student in students:
                    print(
                        f"Имя: {student[0]}, Фамилия: {student[1]}, Страна: {student[4]}, Город: {student[2]}, Площадь города: {student[3]}")
            else:
                print("Ученики не найдены для указанного ID города.")

        except ValueError:
            print("Пожалуйста, введите числовое значение для ID города.")

    conn.close()


if __name__ == "__main__":
    main()
