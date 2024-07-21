from neo4j import GraphDatabase, basic_auth

def create_connection(uri, user, password):
    try:
        driver = GraphDatabase.driver(uri, auth=basic_auth(user, password))
        return driver
    except Exception as e:
        print(f"Failed to create driver: {e}")
        return None

def test_connection(driver):
    try:
        with driver.session() as session:
            result = session.run("RETURN 'Connection successful' AS message")
            for record in result:
                print(record["message"])
        return True
    except Exception as e:
        print(f"Failed to connect to Neo4j: {e}")
        return False

if __name__ == "__main__":
    uri = "bolt://localhost:7687"  # Change this to your Neo4j URI if different
    user = "neo4j"                 # Change this to your Neo4j username if different
    password = "rajesh#1A"          # Change this to your Neo4j password

    driver = create_connection(uri, user, password)
    if driver:
        if test_connection(driver):
            print("Connection to Neo4j established successfully!")
        else:
            print("Connection to Neo4j failed.")
        driver.close()
    else:
        print("Failed to create a connection driver.")
