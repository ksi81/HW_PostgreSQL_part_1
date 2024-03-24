import psycopg2

try:
    conn = psycopg2.connect(
        dbname='postgres',
        user='postgres',
        password='my1111',
        host='localhost',
        port='5432'
    )
    print("З'єднання з базою даних успішне!")
except psycopg2.Error as e:
    print(f"Помилка з'єднання: {e}")