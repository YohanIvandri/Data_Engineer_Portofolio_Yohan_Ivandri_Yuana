import pandas as pd
import sqlite3


def load_to_csv(df, output_path):
    df.to_csv(output_path, index=False)


def load_to_db(df, db_name, table_name):
    sql_connection = sqlite3.connect(db_name)
    df.to_sql(table_name, sql_connection, if_exists='replace', index=False)
    sql_connection.close()


def run_query(query_statement, db_name):
    sql_connection = sqlite3.connect(db_name)
    result = pd.read_sql(query_statement, sql_connection)
    sql_connection.close()
    return result
