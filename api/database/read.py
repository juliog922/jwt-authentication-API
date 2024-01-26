import psycopg2

from api.database.crudbase import CRUDBase

class Read(CRUDBase):
    def get_hashed_password(self, email: str) -> str:
        """Method to get hashed password to compare against real one.

        :param email: User Email
        :type email: str
        :raises psycopg2.OperationalError: In case user dont exist or database error.
        :return: hashed password
        :rtype: str
        """               
        try:
            with psycopg2.connect(self.db_url) as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "SELECT password FROM security WHERE email = %s;",
                        (email,)
                    )
                    hashed_password = cursor.fetchone()[0]
            return hashed_password
        except psycopg2.OperationalError:
            raise 
    
    def check_user_status(self, email: str) -> bool:
        """Know if user active or inactive method.

        :param email: User email
        :type email: str
        :raises psycopg2.OperationalError: In case user dont exist or database error.
        :return: User status
        :rtype: bool
        """               
        try:
            with psycopg2.connect(self.db_url) as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "SELECT active FROM security WHERE email = %s",
                        (email,)
                    )
                    active = cursor.fetchone()[0]
            return bool(active)
        except psycopg2.OperationalError:
            raise 