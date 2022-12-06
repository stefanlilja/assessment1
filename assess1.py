import psycopg2

def get_database_connection():
    return psycopg2.connect(
        host='localhost',
        database='assessment1',
        user='postgres',
        password='continuousimpliesintegrable'
    )

def read_from_database():
    connection = get_database_connection()
    cur=connection.cursor()
    cur.execute('SELECT * FROM view_contacts;')
    rows = cur.fetchall()
    cur.close()
    connection.close()
    for item in rows:
        print(item)

def main():
    read_from_database()

main()