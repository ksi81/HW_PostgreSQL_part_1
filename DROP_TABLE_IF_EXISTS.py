import psycopg2

# Підключення до бази даних
conn = psycopg2.connect(
    dbname='postgres',
    user='postgres',
    password='my1111',
    host='localhost',
    port='5432'
)

# Створення курсора
cur = conn.cursor()

# Видалення таблиці tasks
cur.execute('DROP TABLE IF EXISTS tasks;')

# Видалення таблиці status
cur.execute('DROP TABLE IF EXISTS status;')

# Видалення таблиці users
cur.execute('DROP TABLE IF EXISTS users;')

# Збереження змін у базі даних
conn.commit()

# Закриття з'єднання та курсора
cur.close()
conn.close()

print("Таблиці 'users', 'status', 'tasks' були успішно видалені.")
