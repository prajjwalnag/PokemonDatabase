
# Pokémon Database Optimization Project

## Overview

This project demonstrates the optimization of a Pokémon dataset stored in a SQLite database. It includes scripts for creating the database schema, importing data, analyzing query performance, applying optimizations, and a Continuous Deployment setup using GitHub Actions.

## Getting Started

### Prerequisites

- Python 3.8+
- SQLite3
- Pandas

### Installation

Clone the repository to your local machine:


git clone https://github.com/<your-username>/PokemonDBOptimization.git
cd PokemonDBOptimization

###Install the required Python packages:
pip install -r requirements.txt

##Usage
Create the Database and Import Data

Run the db_creation.py script to create the database schema and data_import.py to import the Pokémon data into the database.

Create the Database and Import Data

Run the db_creation.py script to create the database schema and data_import.py to import the Pokémon data into the database.

bash
Copy code
python scripts/db_creation.py
python scripts/data_import.py
Analyze Performance and Apply Optimizations

Use performance_logging.py to log the initial query performance, and optimization_analysis.py to apply optimizations.



python scripts/performance_logging.py
python scripts/optimization_analysis.py
###Testing

Run tests to ensure the database queries return the expected results.



python -m unittest discover -s tests

##
Continuous Deployment
This project uses GitHub Actions for Continuous Deployment, automatically deploying and testing the latest version on every push to the main branch. The workflow includes steps for environment setup, database schema application, data import, optimization, and testing.

##
Contributing
Contributions are welcome! If you have suggestions for improving the project, please fork the repo and create a pull request or open an issue with the tag "enhancement". Don't forget to give the project a star! Thanks again!

##
License
Distributed under the MIT License. See LICENSE for more information.

##
Acknowledgments
This project uses data from the Pokémon franchise, but is not endorsed by or affiliated with Pokémon, Nintendo, or Game Freak. """