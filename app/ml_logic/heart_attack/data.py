from app.database.connection.create_connection import create_conn
import pandas as pd
from colorama import Fore


def load_data_from_sql():
    conn = create_conn()

    if conn:
        sql_query = "SELECT * FROM dbo.Patients"
        df = pd.read_sql_query(sql_query, conn)
        conn.close()
        return df
    else:
        print(Fore.RED + f'❌Error connecting SQL Server')
