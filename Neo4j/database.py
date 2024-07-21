from neo4j import GraphDatabase, basic_auth

def create_connection():
    driver = GraphDatabase.driver("bolt://localhost:7687", auth=basic_auth("neo4j", "NeoDefault"))
    return driver

def execute_query(driver, query, parameters=None):
    with driver.session() as session:
        session.run(query, parameters)

def fetch_query(driver, query, parameters=None):
    with driver.session() as session:
        result = session.run(query, parameters)
        return [record.data() for record in result]
    
def create_student(driver, student_id, name, age, grade):
    query = "CREATE (s:Student {id: $student_id, name: $name, age: $age, grade: $grade})"
    execute_query(driver, query, {"student_id": student_id, "name": name, "age": age, "grade": grade})

def get_students(driver):
    query = "MATCH (s:Student) RETURN s"
    return fetch_query(driver, query)

def get_student_by_id(driver, student_id):
    query = "MATCH (s:Student {id: $student_id}) RETURN s"
    return fetch_query(driver, query, {"student_id": student_id})

def update_student(driver, student_id, name, age, grade):
    query = "MATCH (s:Student {id: $student_id}) SET s.name = $name, s.age = $age, s.grade = $grade"
    execute_query(driver, query, {"student_id": student_id, "name": name, "age": age, "grade": grade})

def delete_student(driver, student_id):
    query = "MATCH (s:Student {id: $student_id}) DELETE s"
    execute_query(driver, query, {"student_id": student_id})

