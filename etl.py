from elasticsearch import Elasticsearch
import psycopg2

# Подключение к Elasticsearch
es = Elasticsearch("http://localhost:9200")
print(es.info().body)

# Подключение к PostgreSQL
conn = psycopg2.connect(
    dbname="mydatabase",
    user="myuser",
    password="mypassword",
    host="localhost",
    port="5432",
)
cur = conn.cursor()

# SQL запрос для создания таблицы mytable
create_table_query = """
CREATE TABLE mytable (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    age INTEGER
);
"""

# SQL запрос для вставки тестовых данных в таблицу mytable
insert_data_query = """
INSERT INTO mytable (name, age) VALUES
    ('Alice', 30),
    ('Bob', 35),
    ('Charlie', 28),
    ('David', 32);
"""

# Выполнение SQL запросов
try:
    # Выполнение запроса на создание таблицы
    cur.execute(create_table_query)

    # Выполнение запроса на вставку данных
    cur.execute(insert_data_query)

    # Подтверждение транзакции
    conn.commit()
    print("PostgreSQL: Таблица создана и данные добавлены успешно.")

except Exception as error:
    # Откат транзакции в случае ошибки
    conn.rollback()
    print("Произошла ошибка:", error)

# Извлечение данных из PostgreSQL
cur.execute("SELECT * FROM mytable")
rows = cur.fetchall()

# Закрытие соединений
cur.close()
conn.close()

# Трансформация данных (пример трансформации - преобразование данных в JSON)
transformed_data = []
for row in rows:
    transformed_data.append({"id": row[0], "name": row[1], "age": row[2]})


es.indices.create(index="my_index")

# Загрузка данных в Elasticsearch
for item_id, item in enumerate(transformed_data, start=1):
    es.index(
        index="my_index",
        id=str(item_id),
        document=item,
    )

print("Elasticsearch: Индекс создан и данные добавлены успешно.")

result = es.get(index="my_index", id="1")
print("По id=1 найдены данные:", result, sep="\n")
