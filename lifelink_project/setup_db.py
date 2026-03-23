import pymysql
import re

def setup_database():
    # Connect to MySQL server (no database yet)
    connection = pymysql.connect(
        host='localhost',
        user='YOUR_DB_USERNAME_HERE_(Usually "root")',
        password='YOUR_DB_PASSWORD_HERE'
    )
    try:
        with connection.cursor() as cursor:
            cursor.execute('DROP DATABASE IF EXISTS lifelink;')
            cursor.execute('CREATE DATABASE lifelink;')
        connection.commit()
    finally:
        connection.close()

    # Now connecting to the new database
    connection = pymysql.connect(
        host='localhost',
        user='YOUR_DB_USERNAME_HERE_(Usually "root")',
        password='YOUR_DB_PASSWORD_HERE',
        database='lifelink'
    )
    try:
        with connection.cursor() as cursor:
            with open('database/schema.sql', 'r') as file:
                sql = file.read()
                # Removing USE and DB creation statements
                sql = re.sub(r'(?im)^\s*(USE|CREATE DATABASE|DROP DATABASE)[^;]*;?', '', sql)
                # Finding all CREATE TABLE ... ; blocks
                table_statements = re.findall(r'CREATE TABLE[\s\S]+?;(?=\s*CREATE|\s*$)', sql, re.IGNORECASE)
                for stmt in table_statements:
                    cursor.execute(stmt)
            connection.commit()
            print("Database setup completed successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        connection.close()

if __name__ == '__main__':
    setup_database() 