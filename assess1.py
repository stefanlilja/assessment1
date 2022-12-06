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
    cur.execute('SELECT * FROM contacts;')
    rows = cur.fetchall()
    cur.close()
    connection.close()
    for item in rows:
        print(item)

def insert_contact(first_name, last_name, title, organization):
    connection = get_database_connection()
    cur = connection.cursor()
    cur.execute(f"INSERT INTO contacts (first_name, last_name, title, organization) VALUES  ('{first_name}', '{last_name}', '{title}', '{organization}');")
    cur.close()
    connection.commit()
    connection.close()
    print(f'{first_name} {last_name} inserted')

def delete_contact(first_name, last_name):
    connection = get_database_connection()
    cur = connection.cursor()
    cur.execute(f"DELETE FROM contacts WHERE first_name='{first_name}' AND last_name ='{last_name}';")
    cur.close()
    connection.commit()
    connection.close()
    print(f'{first_name} {last_name} deleted')

def main():
    print('Welcome to the contacts list!\nAvailable commands are LIST, INSERT, DELETE, QUIT')
    while True:
        cmd = input('Insert command: ').upper()

        if cmd == 'LIST':
            read_from_database()
        elif cmd == 'QUIT':
            print('Goodbye!')
            break
        elif cmd == 'INSERT':
            first_name = input('Enter first name: ')
            last_name = input('Enter last name: ')
            title = input('Enter title: ')
            organization = input('Enter organization: ')
            insert_contact(first_name, last_name, title, organization)
        elif cmd == 'DELETE':
            first_name = input('Enter first name: ')
            last_name = input('Enter last name: ')
            delete_contact(first_name, last_name)


main()