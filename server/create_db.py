import sys
import logging
import psycopg2

from os import getenv


logger = logging.getLogger()
logger.setLevel(logging.INFO)


def handle():
    print('Starting db creation')
    try:

        connection = psycopg2.connect(dbname='postgres',
                                      user=getenv('DB_USER'), host=getenv('DB_HOST'),
                                      password=getenv('DB_PASSWORD'))
        connection.autocommit = True

        cursor = connection.cursor()

        print("connected to db server")

        cursor.execute('CREATE DATABASE {};'.format(getenv('DB_NAME')))

    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL", error)

        logger.error(
            "ERROR: Unexpected error: Could not connect to postgres instance.")
        sys.exit()
    finally:
        # closing database connection.
        if(connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")


if __name__ == '__main__':
    handle()
