import psycopg2

# Параметры подключения


try:
    conn = psycopg2.connect(
        dbname="senko_tg_bot",
        user="postgres",
        password="",
        host="localhost"
    )
    # Подключение к базе данных
    cur = conn.cursor()
    cur.execute("CREATE TABLE testtable121 (id serial PRIMARY KEY, name varchar);")
    # Выполнение простого запроса
    conn.commit()
    cur.close()
    conn.close()

except psycopg2.Error as ex:
    print("Ошибка подключения к базе данных:", ex)
