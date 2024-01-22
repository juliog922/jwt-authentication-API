import psycopg2

from api.database.crudbase import CRUDBase

class Create(CRUDBase):
    def create_user(self, email: str, password: str, active: bool, admin: bool) -> None:
        """Sign-In Database function.

        :param email: User Email
        :type email: str
        :param password: Hashed Password
        :type password: str
        :param active: User status
        :type active: bool
        :param admin: User Role
        :type admin: bool
        :raises psycopg2.OperationalError: If user already exists or a connection error happens.
        """        
        try:
            connection = psycopg2.connect(self.db_url)
            with connection.cursor() as cursor:
                cursor.execute(
                    "INSERT INTO security (email, password, active, admin) VALUES (%s, %s, %s, %s)",
                    (email, password, active, admin,)
                )
            connection.commit()
            connection.close()
        except psycopg2.OperationalError:
            raise 