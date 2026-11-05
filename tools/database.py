import os
from pathlib import Path

import psycopg
from dotenv import load_dotenv


def insert_data(query, params=None):
    load_dotenv(Path(__file__).resolve().parent / ".env")
    with psycopg.connect(
        user=os.environ["DB_USER"],
        password=os.environ["DB_PASSWORD"],
        host=os.environ["DB_HOST"],
        port=os.environ["DB_PORT"],
        dbname=os.environ["DB_NAME"],
    ) as connection:
        with connection.cursor() as cursor:
            cursor.execute(query, params)
            return cursor.rowcount
