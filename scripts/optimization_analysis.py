import sqlite3
import time

def log_query_performance(db_path='../database/pokemon.db'):
    # Define queries to test performance
    queries = {
        "Find Legendary Pokémon": "SELECT * FROM Pokemon WHERE Legendary = 1",
        "Average Stats by Generation": "SELECT Generation, AVG(Total), AVG(HP), AVG(Attack), AVG(Defense), AVG(SpAtk), AVG(SpDef), AVG(Speed) FROM Pokemon GROUP BY Generation",
        # Add more queries as needed
    }
    
    # Connect to the SQLite database
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Execute each query and log execution time
    for description, query in queries.items():
        start_time = time.time()
        cursor.execute(query)
        cursor.fetchall()  # Assuming we want to fetch results to measure full query execution time
        end_time = time.time()
        
        print(f"{description}: {end_time - start_time:.4f} seconds")
    
    # Close the connection
    conn.close()

def apply_optimizations(db_path='../database/pokemon.db'):
    # Connect to the SQLite database
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Example optimization: Add index to improve the query performance for searching Legendary Pokémon
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_legendary ON Pokemon(Legendary);")
    
    # Example optimization: Add index to improve grouping by Generation
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_generation ON Pokemon(Generation);")
    
    # Commit the changes and close the connection
    conn.commit()
    conn.close()
    
    print("Optimizations applied successfully.")

if __name__ == '__main__':
    print("Logging initial query performance:")
    log_query_performance()
    
    print("\nApplying optimizations...")
    apply_optimizations()
    
    print("\nLogging query performance after optimizations:")
    log_query_performance()
