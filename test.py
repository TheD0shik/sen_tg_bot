import pyodbc

# Параметры подключения
server = 'DESKTOP-VMD5Q4G\\SQLEXPRESS'  
database = 'senko_tg_bot'  
# Строка подключения
connection_string = f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;'

try:
    # Подключение к базе данных
    connection = pyodbc.connect(connection_string)
    cursor = connection.cursor()

    # Выполнение простого запроса
    cursor.execute("SELECT 1")
    result = cursor.fetchone()

    if result:
        print("Подключение успешно и запрос выполнен.")
    else:
        print("Запрос не вернул результатов.")

    # Закрытие подключения
    cursor.close()
    connection.close()

except pyodbc.Error as ex:
    print("Ошибка подключения к базе данных:", ex)