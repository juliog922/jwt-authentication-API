import psycopg2

from api.database.crudbase import CRUDBase

class Update(CRUDBase):
    def user_disabled(self, email: str) -> None:
        """Change user status to inactive

        :param email: User email
        :type email: str
        :raises psycopg2.OperationalError: In case user dont exist or database error
        """              
        try:
            new_status = False
            connection = psycopg2.connect(self.db_url)
            with connection.cursor() as cursor:
                cursor.execute(
                    "UPDATE security SET active = %s WHERE email = %s",
                    (new_status, email,)
                )
            connection.commit()
            connection.close()
        except psycopg2.OperationalError:
            raise 
    
    def user_enabled(self, email: str) -> None:
        """Change user status to active.

        :param email: User email
        :type email: str
        :raises psycopg2.OperationalError: In case user dont exist or database error.
        """              
        try:
            new_status = True
            connection = psycopg2.connect(self.db_url)
            with connection.cursor() as cursor:
                cursor.execute(
                    "UPDATE security SET active = %s WHERE email = %s",
                    (new_status, email,)
                )
            connection.commit()
            connection.close()
        except:
            raise psycopg2.OperationalError
    
    def change_password(self, email: str, password: str) -> None:
        """User change password method.

        :param email: User Email
        :type email: str
        :param password: New hashed password.
        :type password: str
        :raises psycopg2.OperationalError: In case user dont exist or database error.
        """             
        try:
            connection = psycopg2.connect(self.db_url)
            with connection.cursor() as cursor:
                cursor.execute(
                    "UPDATE security SET password = %s WHERE email = %s",
                    (password, email)
                )
            connection.commit()
            connection.close()
        except psycopg2.OperationalError:
            raise 
    