from psycopg2 import connect


conn = connect('postgresql://belhard38:irina@localhost:5432/bh38d1')

with conn.cursor() as cur:
    cur.execute('''
        CREATE TABLE IF NOT EXISTS statuses(
            id SERIAL PRIMARY KEY,
            name VARCHAR(10) NOT NULL UNIQUE
        );
    ''')
    conn.commit()