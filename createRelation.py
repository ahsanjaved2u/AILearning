from neo4j import GraphDatabase
uri = "bolt://localhost:7687"
user = "neo4j"
password = "neoPythonDBMS123456"
driver = GraphDatabase.driver(uri, auth=(user, password))

def run_cypher_query(driver, query, parameters=None):
    with driver.session() as session:
        result = session.run(query, parameters)
        return result

# Example Cypher queries
create_person_query = """
CREATE (p:Person {name: $name, age: $age})
RETURN id(p) AS node_id
"""

create_city_query = """
CREATE (c:City {name: $name})
RETURN id(c) AS node_id
"""

create_relationship_query = """
MATCH (p:Person), (c:City)
WHERE id(p) = $person_id AND id(c) = $city_id
CREATE (p)-[r:LIVES_IN {since: $since}]->(c)
RETURN type(r) AS relationship_type
"""

# Parameters for the queries
person_params = {"name": "Alice", "age": 30}
city_params = {"name": "New York"}
relationship_params = {"since": 2020}

# Create Person node
person_result = run_cypher_query(driver, create_person_query, person_params)
person_id = person_result.single()["node_id"]

# Create City node
city_result = run_cypher_query(driver, create_city_query, city_params)
city_id = city_result.single()["node_id"]

# Create relationship between Person and City
relationship_params.update({"person_id": person_id, "city_id": city_id})
relationship_result = run_cypher_query(driver, create_relationship_query, relationship_params)

print(f"Created a {relationship_result.single()['relationship_type']} relationship between node {person_id} and node {city_id}")

driver.close()

if __name__ == "__main__":
    uri = "bolt://localhost:7687"
    user = "neo4j"
    password = "Pakistan@12345"

    name = 'Ahsan Javes'
    age = 37
    city = 'lahore'
    since = 2000
    get_relation = Neo4jRelation(uri, user, password, name, age, city, since)