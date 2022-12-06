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
    print('Welcome to the contacts list!\nAvailable commands are LIST, INSERT, DELETE, QUIT')
    while True:
        cmd = input('Insert command: ').upper()

        if cmd == 'LIST':
            read_from_database()
        elif cmd == 'QUIT':
            print('Goodbye!')
            break

main()