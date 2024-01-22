import psycopg2

from api.database.crudbase import CRUDBase

class Delete(CRUDBase):
    def delete_user(self, email: str) -> None:
        """Delete user from db.

        :param email: User email
        :type email: str
        :raises psycopg2.OperationalError: In case user dont exist or database error
        """                
        try:
            connection = psycopg2.connect(self.db_url)
            with connection.cursor() as cursor:
                cursor.execute(
                    "DELETE FROM security WHERE email = %s",
                    (email,)
                )
            connection.commit()
            connection.close()
        except psycopg2.OperationalError:
            raise 