import sqlite3
import time

def log_query_performance(db_path='../database/pokemon.db'):
    queries = [
        "SELECT * FROM Pokemon WHERE Legendary = 1;",
        "SELECT TypeName, COUNT(*) as PokemonCount FROM Pokemon JOIN PokemonType ON Pokemon.Type1ID = PokemonType.TypeID GROUP BY TypeName;",
        "SELECT Generation, AVG(Total) FROM Pokemon GROUP BY Generation;"
    ]

    # Connect to the SQLite database
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    for query in queries:
        start_time = time.time()
        cursor.execute(query)
        cursor.fetchall()  # Fetch results to ensure the query is fully executed
        end_time = time.time()
        print(f"Query: {query}\nExecution Time: {end_time - start_time} seconds\n")

    conn.close()

if __name__ == '__main__':
    log_query_performance()