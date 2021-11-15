from .database import Database

db = None
class DbFactory():
    global db
    @staticmethod
    def set_db_instance(db1):
        DbFactory.db = db1

    @staticmethod
    def get_db_instance():
        if DbFactory.db is None:
            DbFactory.db = Database()
        return DbFactory.db