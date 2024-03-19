import pandas as pd
from sqlalchemy import create_engine

# Path to your Excel file
excel_file = 'sample.xlsx'

# Database connection parameters
db_username = 'your_username'
db_password = 'your_password'
db_host = 'localhost'
db_port = '5432'  # Change this port to your database port
db_name = 'your_database_name'

# SQLAlchemy connection string
connection_str = f'postgresql://{db_username}:{db_password}@{db_host}:{db_port}/{db_name}'

# Create a database engine
engine = create_engine(connection_str)

# Specify the columns you want to load from Excel
columns_to_load = ['column1', 'column2', 'column3']  # Add your desired column names here

# Load data from Excel into a DataFrame with specific columns
df = pd.read_excel(excel_file, usecols=columns_to_load)

# Define the table name in the database
table_name = 'sample_table'

# Write the data from the DataFrame to the SQL database
df.to_sql(table_name, engine, index=False, if_exists='append')

print("Data loaded successfully into the SQL database.")
