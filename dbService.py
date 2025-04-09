import mysql.connector
from rich import print


def createConnection():
    conn = mysql.connector.connect(
        host = "localhost",
        port = 3306,
        user="mhemanthkmr",
        password="Hemanth123$",
        database = "shop"
    )
    conn.autocommit = True
    return conn

def formatter(cursor, data):  
    result = []

    for row in data:
        row_dict = {}
        for idx, column in enumerate(cursor.description):
            row_dict[column[0]] = row[idx]
        result.append(row_dict)

    return result


def fetchData(id):
    print(id)
    conn = createConnection()
    cursor = conn.cursor()
    cursor.execute(f"select * from cutomer_data where customer_id = {id}")
    data = cursor.fetchall()
    # print(formatter(cursor, data))
    return formatter(cursor, data)

