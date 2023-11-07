from app.database.connection.create_connection import test_connection
from colorama import Fore, Style

def main():
    import argparse

    parser = argparse.ArgumentParser(description='Execute methods from the script')
    parser.add_argument('--method', choices=['test_connection'], help='Method to execute')

    args = parser.parse_args()

    if args.method == 'test_connection':
        test_connection()
    else:
        print(Fore.RED + "Method not found" + Style.RESET_ALL)

if __name__ == '__main__':
    main()
