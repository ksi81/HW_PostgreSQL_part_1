import psycopg2

# Параметри підключення до бази даних
conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="my1111",
    host="localhost",
    port="5432"
)

# Курсор для виконання SQL запитів
cur = conn.cursor()

# Читаємо SQL скрипт для створення таблиць
with open("create_tables.sql", "r") as sql_file:
    sql_script = sql_file.read()

# Виконуємо SQL скрипт
cur.execute(sql_script)

# Зберігаємо зміни
conn.commit()

# Закриваємо з'єднання
cur.close()
conn.close()
