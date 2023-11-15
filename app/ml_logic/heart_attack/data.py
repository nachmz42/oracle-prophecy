from app.database.connection.create_connection import create_conn
import pandas as pd
from colorama import Fore
from app.environment.params import DATA_ORIGIN, DATA_DIRECTORY_HEART_ATTACK, HEART_ATTACK_COLUMNS_CSV

def load_data():

    if DATA_ORIGIN == 'sql':
        conn = create_conn()
        if conn:
                sql_query = "SELECT * FROM dbo.HeartAttack"
                df = pd.read_sql_query(sql_query, conn)
                conn.close()
                return df
        else:
            print(Fore.RED + f'❌Error connecting SQL Server')
    if DATA_ORIGIN == 'csv':
        df = pd.read_csv(DATA_DIRECTORY_HEART_ATTACK)
        df.columns = HEART_ATTACK_COLUMNS_CSV
        return df
