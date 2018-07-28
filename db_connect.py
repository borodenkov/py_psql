# Импортируем библиотеку, соответствующую типу нашей базы данных 
import sqlite3

# conn = psycopg2.connect( host=hostname, user=username, password=password, dbname=database)


if __name__ == '__main__':
    # Создаем соединение с нашей базой данных
    # В нашем примере у нас это просто файл базы
    conn = sqlite3.connect('chinook.db')

    # Создаем курсор - это специальный объект который делает запросы и получает их результаты
    cursor = conn.cursor()
    print(cursor)
    # Делаем SELECT запрос к базе данных, используя обычный SQL-синтаксис
    cursor.execute("SELECT Name FROM artists ORDER BY Name LIMIT 3")

    # Получаем результат сделанного запроса
    results = cursor.fetchall()
    results2 = cursor.fetchall()

    print(results)  # [('A Cor Do Som',), ('Aaron Copland & London Symphony Orchestra',), ('Aaron Goldberg',)]
    print(results2)  # []
    cursor.execute("INSERT INTO artists VALUES (NULL, 'A Aagrh!') ")

    # Если мы не просто читаем, но и вносим изменения в базу данных - необходимо сохранить транзакцию
    conn.commit()

    # Проверяем результат
    cursor.execute("SELECT Name FROM artists ORDER BY Name LIMIT 3")
    results = cursor.fetchall()
    print(results)

    # ТУТ БУДЕТ НАШ КОД РАБОТЫ С БАЗОЙ ДАННЫХ
    # КОД ДАЛЬНЕЙШИХ ПРИМЕРОВ ВСТАВЛЯТЬ В ЭТО МЕСТО

    cursor.executescript("""
     insert into artists values (Null, 'A Aagrh!');
     insert into artists values (Null, 'A Aagrh-2!');
    """)

    cursor.execute("SELECT Name FROM artists ORDER BY Name LIMIT ?", ('2'))

    # И с использованием именнованных замен:
    cursor.execute("SELECT Name FROM artists ORDER BY Name LIMIT :limit", {"limit": 3})

    cursor.execute("SELECT Name FROM artists ORDER BY Name LIMIT 3")
    print(cursor.fetchone())  # ('A Cor Do Som',)
    print(cursor.fetchone())  # ('Aaron Copland & London Symphony Orchestra',)
    print(cursor.fetchone())  # ('Aaron Goldberg',)
    print(cursor.fetchone())  # None

    for row in cursor.execute('SELECT Name FROM artists ORDER BY Name LIMIT 300'):
        print(row)

    # Не забываем закрыть соединение с базой данных
    conn.close()
