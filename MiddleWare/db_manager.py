from getpass import getpass
from mysql.connector import connect, Error

"""QUERY DEFINITIONS"""


class DBManager:
    QUERY_CREATE_DB = "CREATE DATABASE"
    QUERY_SHOW_ALL_DB = "SHOW DATABASES"

    def __init__(self, username: str, password: str):
        self.session = None
        self.cursor = None
        self.connect_session(username, password)

    def __del__(self):
        print("Closing DB session")
        if self.session is not None:
            self.close_session()

    #################### SESSION SECTION ####################
    def connect_session(self, username: str, password: str, host: str = "localhost", db_name: str = None):
        try:
            if db_name is None:
                self.session = connect(host=host, user=username, password=password)
            else:
                self.session = connect(host=host, user=username, password=password, database=db_name)

            if self.session is not None:
                print("Login successful", self.session)
                self.cursor = self.session.cursor()

        except Error as e:
            print("Login failed:", e)

    def close_session(self):
        self.session.close()
        self.session = None

    #################### DATABASE SECTION ####################
    def db_create(self, db_name: str):
        db_name = " " + db_name
        self.cursor.execute(self.QUERY_CREATE_DB + db_name)

    def db_connect(self, db_name: str):
        db_name = " " + db_name
        self.cursor.execute(self.QUERY_CREATE_DB + db_name)

    def db_show_all(self):
        self.cursor.execute(self.QUERY_SHOW_ALL_DB)

        database_list = [item for item in self.cursor]
        return database_list


if __name__ == '__main__':
    username = input("Enter username: ")
    password = input("Enter password: ")

    DB = DBManager(username, password)
    db_list = DB.db_show_all()
    print("[RESP]=", db_list)

    DB.close_session()
