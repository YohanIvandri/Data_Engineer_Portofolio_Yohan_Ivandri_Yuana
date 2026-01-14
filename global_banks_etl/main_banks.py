from datetime import datetime
from src.extract_banks import extract
from src.transform_banks import transform
from src.load_banks import load_to_csv, load_to_db, run_query


csv_path = './data/exchange_rate.csv'
output_path = './data/Largest_banks_data.csv'
table_name = 'Largest_banks'
db_name = './db/Banks.db'
LOG_PATH = "./logs/codelog.txt"

def log_progress(message):
    timestamp = datetime.now().strftime("%Y-%h-%d-%H:%M:%S")
    with open(LOG_PATH, "a") as log:
        log.write(f"{timestamp} : {message}\n")


# Preliminaries
log_progress("Preliminaries complete. Initiating ETL process")

# Extract
df = extract()
log_progress("Data extraction complete. Initiating Transformation process")

# Transform
df = transform(df, csv_path)
log_progress("Data transformation complete. Initiating Loading process")

# Load to CSV
load_to_csv(df, output_path)
log_progress("Data saved to CSV file")

# Load to Database
log_progress("SQL Connection initiated")
load_to_db(df, db_name, table_name)
log_progress("Data loaded to Database as a table, Executing queries")

# Run Queries
print(run_query(f"SELECT * FROM {table_name}", db_name))
print(run_query(f"SELECT AVG(MC_GBP_Billion) FROM {table_name}", db_name))
print(run_query(f"SELECT Country FROM {table_name} LIMIT 5", db_name))

log_progress("Process Complete")
log_progress("Server Connection closed")
