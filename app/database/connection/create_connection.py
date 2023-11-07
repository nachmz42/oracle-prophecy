import pyodbc
from app.environment.params import SERVER, DATABASE, USERNAME, PASSWORD, PORT
from colorama import Fore, Style



server = SERVER
database = DATABASE
username = USERNAME
password = PASSWORD
port = PORT

connection_string = f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server},{port};DATABASE={database};UID={username};PWD={password}"

def create_conn():
    try:
        print(Fore.GREEN + f"Starting the connection to {SERVER}:{PORT}" + Style.RESET_ALL)
        conn = pyodbc.connect(connection_string)
        print(Fore.GREEN + "✅Successful connection to SQL Server"+ Style.RESET_ALL)
        return conn



    except pyodbc.Error as ex:
        print(Fore.RED + f'❌Error connecting SQL Server with: server -> {server} | database -> {database} | port -> {port}' + Style.RESET_ALL, ex)
        return None

def test_connection():
    conn = create_conn()
    if conn != None :
        conn.close()
