# Required packages
from pathlib import Path
import sqlite3
import pandas as pd

# use pathlib to get current working directory
path = Path.cwd()


def create_db(db_name, filename, table_name):
    # create a path to the data file
    file_path = path / filename

    # create a connection to the database
    conn = sqlite3.connect(db_name)
    # create a cursor
    cur = conn.cursor()

    # read in the data 
    movies = pd.read_csv(file_path)
    
    # insert the data into the specified table
    movies.to_sql(table_name, conn, index=False, if_exists="replace")
    
    # execute a select statement as f-string and print results to verify insertion
    rows = cur.execute(f"SELECT * FROM {table_name}").fetchall()
    print(rows)

    # commit the changes to the database
    conn.commit()
    # close the connection
    conn.close()


if __name__=="__main__":
    db_name = "MCU.db"
    filename = "MCU_Data.csv"
    table_name = "movies"
    create_db(db_name, filename, table_name)