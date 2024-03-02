import sqlite3

# Connect to SQLite database (or create it if it does not exist)
conn = sqlite3.connect('../database/pokemon.db')
cursor = conn.cursor()

# Create the PokemonType table
cursor.execute('''
CREATE TABLE IF NOT EXISTS PokemonType (
    TypeID INTEGER PRIMARY KEY AUTOINCREMENT,
    TypeName TEXT NOT NULL UNIQUE
);
''')

# Create the Pokemon table
cursor.execute('''
CREATE TABLE IF NOT EXISTS Pokemon (
    PokemonID INTEGER PRIMARY KEY,
    Name TEXT NOT NULL,
    Type1ID INTEGER,
    Type2ID INTEGER,
    Total INTEGER,
    HP INTEGER,
    Attack INTEGER,
    Defense INTEGER,
    SpAtk INTEGER,
    SpDef INTEGER,
    Speed INTEGER,
    Generation INTEGER,
    Legendary BOOLEAN,
    FOREIGN KEY(Type1ID) REFERENCES PokemonType(TypeID),
    FOREIGN KEY(Type2ID) REFERENCES PokemonType(TypeID)
);
''')

# Commit changes and close the connection
conn.commit()
conn.close()

print("Database and tables created successfully.")