import os

import psycopg2

class Postgres:
    def __init__(self) -> None:
        """Contains postgre url as attribute.
        """        
        self.db_url = "postgresql://{}:{}@{}/{}".format(
        os.environ.get("POSTGRES_USER"),
        os.environ.get("POSTGRES_PASSWORD"),
        os.environ.get("POSTGRES_NAME"),
        os.environ.get("POSTGRES_DB"),
    )
    def check_db_connection(self) -> bool:
        """Check Database Connection.

        :return: Confirmation of Database Server is running healthy.
        :rtype: bool
        """        
        try:
            conn = psycopg2.connect(self.db_url)
            cursor = conn.cursor()
            cursor.execute("SELECT 1+1")
            conn.closed
            return True
        except psycopg2.OperationalError:
            return False

postgres_controler = Postgres()