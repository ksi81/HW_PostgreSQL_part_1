from faker import Faker
import psycopg2

fake = Faker()

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

# Заповнення таблиці status з перевіркою на унікальність
status_values = ['new', 'in progress', 'completed']
for status in status_values:
    cur.execute("SELECT id FROM status WHERE name = %s", (status,))
    existing_status = cur.fetchone()
    if not existing_status:
        cur.execute("INSERT INTO status (name) VALUES (%s)", (status,))

# Заповнення таблиці users
user_count = 0
for _ in range(10):
    fullname = fake.name()
    email = fake.email()
    cur.execute("SELECT id FROM users WHERE email = %s", (email,))
    existing_user = cur.fetchone()
    if not existing_user:
        cur.execute('INSERT INTO users (fullname, email) VALUES (%s, %s)', (fullname, email))
        user_count += 1

# Заповнення таблиці tasks
task_count = 0
for _ in range(20):
    title = fake.text(max_nb_chars=50)
    description = fake.text()
    status_id = fake.random_int(min=1, max=3)
    user_id = fake.random_int(min=1, max=10)
    cur.execute('INSERT INTO tasks (title, description, status_id, user_id) VALUES (%s, %s, %s, %s)',
                (title, description, status_id, user_id))
    task_count += 1

# Збереження змін у базі даних
conn.commit()

# Закриття з'єднання та курсора
cur.close()
conn.close()

print(f"Таблиця 'users' успішно заповнена. Додано {user_count} записів.")
print(f"Таблиця 'status' успішно заповнена. Додано {len(status_values)} записи.")
print(f"Таблиця 'tasks' успішно заповнена. Додано {task_count} записів.")
