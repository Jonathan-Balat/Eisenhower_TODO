from mysql.connector import connect, Error

"""
    REFERENCES:
        - https://dev.mysql.com/doc/refman/5.7/en/data-types.html
"""


class DBManager:
    QUERY_DB_DICT = \
        {
            "create":   "CREATE DATABASE",
            "delete":   "DROP DATABASE [IF EXISTS]",
            "connect":  "USE",
            "show_all_db": "SHOW DATABASES",
            "show_all_table": "SHOW TABLES"
        }

    def __init__(self):
        self.session = None
        self.cursor = None

    def __del__(self):
        print("Closing DB session")
        if self.session is not None:
            self.close_session()

    #################### SESSION SECTION ####################
    def connect_session(self, username: str, password: str, host: str = "localhost", db_name: str = None):
        try:
            b_logged_in = False

            if db_name is None:
                self.session = connect(host=host, user=username, password=password)
            else:
                self.session = connect(host=host, user=username, password=password, database=db_name)

            if self.session is not None:
                b_logged_in = True
                print("Login successful", self.session)
                self.cursor = self.session.cursor()

        except Error as e:
            b_logged_in = False
            self.session = None
            print("Login failed:", e)

        finally:
            return b_logged_in

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

    #################### TABLE SECTION ####################
    #################### RAW COMMAND SECTION ####################
    def command(self, cmd):
        self.cursor.execute(cmd)
        return [item for item in self.cursor]


if __name__ == '__main__':
    cmd_mode = True

    user = input("Enter username: ")
    pw = input("Enter password: ")

    DB = DBManager()
    b_logged_in = DB.connect_session(user, pw)

    if b_logged_in:
        if cmd_mode:
            ret_val = ""

            while True:
                cmd = input(">> ")
                if cmd == "exit":
                    break
                ret_val = DB.command(cmd)
                print("RET = ", ret_val)

        else:
            db_list = DB.db_command("show_all_db")
            print("[RESP]=", db_list)

            DB.db_command("connect", "todo_dev")
            db_list = DB.db_command("show_all_table")
            print("[RESP]=", db_list)

        DB.close_session()
