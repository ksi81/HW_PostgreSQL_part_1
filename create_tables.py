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

# Створення таблиці users
cur.execute('''
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    fullname VARCHAR(100),
    email VARCHAR(100) UNIQUE
);
''')

# Створення таблиці status
cur.execute('''
CREATE TABLE IF NOT EXISTS status (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) UNIQUE
);
''')

# Створення таблиці tasks зі зв'язками до таблиць status та users
cur.execute('''
CREATE TABLE IF NOT EXISTS tasks (
    id SERIAL PRIMARY KEY,
    title VARCHAR(100),
    description TEXT,
    status_id INTEGER REFERENCES status(id) ON DELETE CASCADE,
    user_id INTEGER REFERENCES users(id) ON DELETE CASCADE
);
''')

# Збереження змін у базі даних
conn.commit()

# Отримання інформації про поля та їх типи
cur.execute("SELECT column_name, data_type FROM information_schema.columns WHERE table_name = 'users' OR table_name = 'status' OR table_name = 'tasks'")
columns_info = cur.fetchall()

# Виведення інформації про поля та їх типи
for column_info in columns_info:
    print(f"Поле: {column_info[0]}, Тип: {column_info[1]}")

# Закриття з'єднання та курсора
cur.close()
conn.close()

print("Таблиці 'users', 'status', 'tasks' були успішно створені з врахуванням взаємозв'язків.")
