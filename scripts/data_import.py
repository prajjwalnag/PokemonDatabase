import pandas as pd
import sqlite3

def import_data(db_path='../database/pokemon.db', csv_path='../database/Pokemon.csv'):
    # Load the dataset
    df = pd.read_csv(csv_path)

    # Connect to the SQLite database
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Insert unique types into the PokemonType table
    unique_types = pd.unique(df[['Type 1', 'Type 2']].values.ravel('K'))
    for type_name in unique_types:
        if pd.notna(type_name):  # Ensure the type name is not NaN
            cursor.execute('INSERT OR IGNORE INTO PokemonType (TypeName) VALUES (?);', (type_name,))

    # Commit the insertions to the PokemonType table
    conn.commit()

    # Function to get TypeID from TypeName
    def get_type_id(type_name):
        cursor.execute('SELECT TypeID FROM PokemonType WHERE TypeName = ?;', (type_name,))
        result = cursor.fetchone()
        return result[0] if result else None

    # Import data into the Pokemon table using INSERT OR REPLACE
    for _, row in df.iterrows():
        type1_id = get_type_id(row['Type 1'])
        type2_id = get_type_id(row['Type 2']) if pd.notna(row['Type 2']) else None
        cursor.execute('''
        INSERT OR REPLACE INTO Pokemon (PokemonID, Name, Type1ID, Type2ID, Total, HP, Attack, Defense, SpAtk, SpDef, Speed, Generation, Legendary)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
        ''', (row['#'], row['Name'], type1_id, type2_id, row['Total'], row['HP'], row['Attack'], row['Defense'], row['Sp. Atk'], row['Sp. Def'], row['Speed'], row['Generation'], int(row['Legendary'])))

    # Commit the insertions to the Pokemon table
    conn.commit()

    # Close the connection
    conn.close()

    print("Data imported successfully into the database.")

if __name__ == '__main__':
    import_data()
