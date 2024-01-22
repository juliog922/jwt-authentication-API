import os

import psycopg2

from api.database.create import Create
from api.database.read import Read
from api.database.update import Update
from api.database.delete import Delete

class Postgres:
    """Postgres database connection.
    """    
    def __init__(self) -> None:
        """Contains postgre url as attribute and CRUD instances.
        """        
        self.db_url = "postgresql://{}:{}@{}/{}".format(
        os.environ.get("POSTGRES_USER"),
        os.environ.get("POSTGRES_PASSWORD"),
        os.environ.get("POSTGRES_NAME"),
        os.environ.get("POSTGRES_DB"),
    )
        self.creator = Create(self.db_url)
        self.reader = Read(self.db_url)
        self.updater = Update(self.db_url)
        self.deleter = Delete(self.db_url)

    def get_connection(self):
        """Give connection to CRUD functions.

        :return: Postgres Database connection
        :rtype: psycopg2.connection
        """        
        return psycopg2.connect(self.db_url)
    
    def check_db_connection(self) -> bool:
        """Check Database Connection.

        :return: Confirmation of Database Server is running healthy.
        :rtype: bool
        """        
        try:
            conn = self.get_connection()
            conn.close()
            return True
        except psycopg2.OperationalError:
            return False
    
    def create_security_table(self) -> None:
        """Create 'security' table if not exists.

        This method creates the 'security' table with the specified fields:
        - id: Numeric, auto-increment, primary key
        - email: Varchar(50), unique
        - password: Varchar(50)
        - active: Boolean
        - admin: Boolean
        """        
        conn = self.get_connection()
        cursor = conn.cursor()

        # SQL query to create 'security' table
        create_table_query = '''
            CREATE TABLE IF NOT EXISTS security (
                id SERIAL PRIMARY KEY,
                email VARCHAR(50) UNIQUE NOT NULL,
                password VARCHAR(50) NOT NULL,
                active BOOLEAN,
                admin BOOLEAN
            );
        '''

        cursor.execute(create_table_query)
        conn.commit()
        conn.close()


postgres_controler = Postgres()