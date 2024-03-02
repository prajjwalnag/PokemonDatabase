import unittest
import sqlite3
import time

class PokemonDatabaseTests(unittest.TestCase):
    db_path = '../database/pokemon.db'

    @classmethod
    def setUpClass(cls):
        cls.conn = sqlite3.connect(cls.db_path)
        cls.cursor = cls.conn.cursor()

    @classmethod
    def tearDownClass(cls):
        cls.conn.close()

    def test_legendary_pokemon_query(self):
        """Test that the query to find legendary Pokémon executes successfully."""
        query = "SELECT * FROM Pokemon WHERE Legendary = 1"
        start_time = time.time()
        self.cursor.execute(query)
        results = self.cursor.fetchall()
        end_time = time.time()
        execution_time = end_time - start_time

        # Check that the query returns results
        self.assertTrue(len(results) > 0, "Query for legendary Pokémon should return results.")
        # Optionally, check the execution time is below a threshold
        self.assertLess(execution_time, 1, "Query for legendary Pokémon should be fast.")

    def test_average_stats_by_generation(self):
        """Test that the query to calculate average stats by generation executes successfully."""
        query = "SELECT Generation, AVG(Total), AVG(HP), AVG(Attack), AVG(Defense), AVG(SpAtk), AVG(SpDef), AVG(Speed) FROM Pokemon GROUP BY Generation"
        start_time = time.time()
        self.cursor.execute(query)
        results = self.cursor.fetchall()
        end_time = time.time()
        execution_time = end_time - start_time

        # Check that the query returns results for all generations
        self.assertTrue(len(results) >= 1, "Query for average stats by generation should return results.")
        # Optionally, check the execution time is below a threshold
        self.assertLess(execution_time, 1, "Query for average stats by generation should be fast.")

# Add more tests as necessary

if __name__ == '__main__':
    unittest.main()
