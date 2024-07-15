import psycopg2
from psycopg2 import Error, OperationalError

def create_connection():
    connection = None
    try:
        connection = psycopg2.connect(
            host="localhost",
            user="postgres",
            password="root",
            database="school"
        )
        print("Connection to PostgreSQL DB successful")
    except OperationalError as e:
        print(f"The error '{e}' occurred")
    return connection

def execute_query(connection, query, values=None):
    cursor = connection.cursor()
    try:
        if values:
            cursor.execute(query, values)
        else:
            cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")

def fetch_query(connection, query, values=None):
    cursor = connection.cursor()
    result = None
    try:
        if values:
            cursor.execute(query, values)
        else:
            cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")
        return None
    
def create_student(connection, name, age, grade):
    query = "INSERT INTO students (name, age, grade) VALUES (%s, %s, %s)"
    values = (name, age, grade)
    execute_query(connection, query, values)

def get_students(connection):
    query = "SELECT * FROM students"
    return fetch_query(connection, query)

def get_student_by_id(connection, student_id):
    query = "SELECT * FROM students WHERE id = %s"
    values = (student_id,)
    return fetch_query(connection, query, values)

def update_student(connection, student_id, name, age, grade):
    query = "UPDATE students SET name = %s, age = %s, grade = %s WHERE id = %s"
    values = (name, age, grade, student_id)
    execute_query(connection, query, values)

def delete_student(connection, student_id):
    query = "DELETE FROM students WHERE id = %s"
    values = (student_id,)
    execute_query(connection, query, values)
