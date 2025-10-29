import mysql.connector

def insert_data(data):
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Abhi07mh45",
        database="scada_database"
    )
    cursor = conn.cursor()

    # Example: assuming SCADA sends {"tag": "Pump1", "value": 25.6}
    query = "INSERT INTO scada_db.scada_data (tag, value) VALUES (%s, %s)"
    values = (data.get("tag"), data.get("value"))


    cursor.execute(query, values)
    conn.commit()
    cursor.close()
    conn.close()
