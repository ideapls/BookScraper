import json
import pyodbc
import os

with open("../output.json", "r", encoding='utf-8') as json_file:
    data = json.load(json_file)


def quantity_validation():
    for item in data:
        if item['availability'] == 'Instock':
            quantity = str(item['quantity'])
            quantity = quantity.split("a")[0]
            return quantity
        else:
            return 0


db_login = os.environ.get('DB_LOGIN')
db_password = os.environ.get('DB_PASSWORD')

conn = pyodbc.connect(
    'DRIVER={SQL Server};SERVER=DESKTOP-RVT84EK;DATABASE=ScrappedBooks;UID=%s;PWD=%s' % (db_login, db_password))
cursor = conn.cursor()

cursor.execute("""CREATE TABLE books (
                    id INT IDENTITY(1,1) PRIMARY KEY,
                    title NVARCHAR(250),
                    price NVARCHAR(7),
                    availability NVARCHAR(10),
                    quantity INT)""")

for item in data:
    cursor.execute('INSERT INTO books (title, price, availability, quantity) VALUES (?, ?, ?, ?)', (item['title'],
                                                                                                    item['price'],
                                                                                                    item[
                                                                                                        'availability'],
                                                                                                    quantity_validation()))

conn.commit()
conn.close()
