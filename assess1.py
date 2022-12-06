import psycopg2

def get_database_connection():
    return psycopg2.connection(
        host='localhost',
        database='assessment1',
        user='postgres',
        password='continuousimpliesintegrable'
    )

