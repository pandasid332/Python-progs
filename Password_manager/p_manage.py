import psycopg2
import configparser

conn = None   
cur = None

# Read the configuration file
config = configparser.ConfigParser()
config.read('db_config.ini')

# Get the database credentials
db_host = config['postgresql_db']['host']
db_port = config['postgresql_db']['port']
db_database = config['postgresql_db']['database']  # Corrected variable name
db_user = config['postgresql_db']['username']
db_password = config['postgresql_db']['password']

try:
    with psycopg2.connect(host=db_host, port=db_port, database=db_database, user=db_user, password=db_password) as conn:
        with conn.cursor() as cur:
            cur.execute('DROP TABLE IF EXISTS teacher')
            create_table_query = '''CREATE TABLE IF NOT EXISTS teacher
            (id int PRIMARY KEY,
            name VARCHAR(100))'''
            cur.execute(create_table_query)
            
            insert_query = '''INSERT INTO teacher (id,name) 
            VALUES (%s, %s)'''
            record_to_insert = [(1,'abc'), (2,'def'), (3,'ghi'), (4,'jkl')]
            
            for rec in record_to_insert:
                cur.execute(insert_query, rec)
                
            updated_query = '''UPDATE teacher SET name = 'Sid' WHERE id = %s'''
            record_to_update = [(1,),(2,)]
            
            for rec in record_to_update:
                cur.execute(updated_query, rec)
            
            
except psycopg2.Error as e:
    print('Error occurred:', e)
else:
    print()
    print('--------------------------------------------')
    print('Table created successfully')
    print('--------------------------------------------')
    print('Data inserted successfully')
    print('--------------------------------------------')
    print('Data updated successfully')
    print()
finally:
    if conn is not None:
        conn.close()
        print('Database connection closed')