from app.database.connection.create_connection import test_connection


def main():
    import argparse

    parser = argparse.ArgumentParser(description='Ejecutar métodos en el script')
    parser.add_argument('--method', choices=['test_connection'], help='El método a ejecutar')

    args = parser.parse_args()

    if args.method == 'test_connection':
        test_connection()
    else:
        print("Método no válido.")

if __name__ == '__main__':
    main()
