
# !pip install tabula-py

import mysql.connector
import tabula
tables = tabula.read_pdf(
    './sum23.pdf', pages='all')

all_data = []
for table in tables:
    for row in table.values.tolist():
        all_data.append(row)

# print(all_data)


mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="neub_result"
)

cursor = mydb.cursor()

for row in all_data:
    print(row)
    # sql = "INSERT INTO table_x VALUES ({})".format(placeholders)
    # cursor.execute(sql, row)

# mydb.commit()

# print(cursor.rowcount, "record inserted.")

# mydb.close()
