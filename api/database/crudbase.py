class CRUDBase:
    """Base Class for CRUD Methods.
    """    
    def __init__(self, db_url: str) -> None:
        """Contains postgres connection url as attribute to share

        :param db_url: url of database server

        :type db_url: str
        """               
        self.db_url = db_url