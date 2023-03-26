from mysql.connector import connect, Error

"""QUERY DEFINITIONS"""


class DBManager:
    QUERY_DB_DICT = \
        {
            "create":   "CREATE DATABASE",
            "delete":   "DROP DATABASE [IF EXISTS]",
            "connect":  "USE",
            "show_all_db": "SHOW DATABASES",
            "show_all_table": "SHOW TABLES"
        }

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
    def db_command(self, cmd: str, str_cmd: str = None):
        ret_val = None

        db_cmd = self.QUERY_DB_DICT.get(cmd)

        if db_cmd is not None:
            if str_cmd is None:
                self.cursor.execute(db_cmd)
            else:
                self.cursor.execute(db_cmd + " " + str_cmd)
            ret_val = [item for item in self.cursor]

        return ret_val

    #################### RAW COMMAND SECTION ####################
    def command(self, cmd):
        self.cursor.execute(cmd)
        return [item for item in self.cursor]


if __name__ == '__main__':
    cmd_mode = True

    username = input("Enter username: ")
    password = input("Enter password: ")

    DB = DBManager(username, password)

    if cmd_mode:
        ret_val = ""

        while True:
            cmd = input(">> ")
            ret_val = DB.command(cmd)
            print("RET = ", ret_val)

    else:
        db_list = DB.db_command("show_all_db")
        print("[RESP]=", db_list)

        db_list = DB.db_command("connect", "todo_dev")
        db_list = DB.db_command("show_all_table")
        print("[RESP]=", db_list)

    DB.close_session()
