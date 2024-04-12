import sqlite3
from datetime import datetime

from constans import url, emoji
from utilities.log_class import LogClass


class DatabaseManipulating:
    log: LogClass
    connection: sqlite3.Connection
    cursor: sqlite3.Cursor
    flag: set()

    def __init__(self, log):
        self.log = log

    def create_database(self):
        try:
            self.connection = sqlite3.connect(url.DATABASE_URI)
            self.cursor = self.connection.cursor()
            self.log.info(f"connected to SQLite successfully {emoji.TASK_SUCCSEEDED}")
        except sqlite3.OperationalError as oe:
            self.log.critical(f"Failed to connect to database {emoji.TASK_FAILED}."
                              f" Operational error: {oe}")
        except sqlite3.DatabaseError as de:
            self.log.critical(f"Failed to connect to database {emoji.TASK_FAILED}. "
                              f"Database error: {de}")
        except Exception as e:
            self.log.critical(f"failed to connect to database {emoji.TASK_FAILED}. The error: {e}")

    def input_data_into_database_table(self, data):
        try:
            for hour, all_minutes in data:
                for minutes in all_minutes:
                    self.cursor.execute('INSERT INTO my_table (hour, minutes) VALUES (?, ?)',
                                        (hour, minutes))
            self.connection.commit()
            self.log.info(f"Inserted data into database successfully {emoji.INFO} ")
        except sqlite3.Error as e:
            self.log.critical(f"failed to insert data into database{emoji.TASK_FAILED}. Error: {e}")

    def close_database(self):
        self.connection.close()
        self.log.debug(f"database closed {emoji.TASK_SUCCSEEDED}")

    def create_database_table(self):
        self.connection = sqlite3.connect(url.DATABASE_URI)
        self.cursor = self.connection.cursor()
        try:
            self.cursor.execute('DROP table my_table')
            self.cursor.execute('''CREATE TABLE my_table (
                                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                                        hour INTEGER,
                                        minutes TEXT
                                    )''')
            self.log.debug(f"my_table was replaced with new table "
                           f"under same name{emoji.TASK_SUCCSEEDED}")
        except Exception as e:
            self.log.critical(f"An unexpected error occurred: {e}")

    def get_selected_hour_data_into_list(self, index):
        self.cursor.execute(f'SELECT minutes FROM my_table WHERE hour == {index}')
        selected_hour_times = self.cursor.fetchall()
        selected_hour_schedule = []
        for times in selected_hour_times:
            selected_hour_schedule.append(times[0])
        if not selected_hour_schedule:
            self.log.critical(f"failed to gather information for database {emoji.TASK_FAILED}")
        return selected_hour_schedule

    def get_data_from_database(self):
        hour = datetime.now().hour
        time_table = []
        self.flag = set()
        for index in range(hour - 1, hour + 2):
            new_hour = self.get_selected_hour_data_into_list(index)
            # this for loop checks if there are any duplicating minutes
            for hour_table in time_table:
                # lambda converts lists to sets and checks is there intersection ( same values)
                # and if do, adds hour to flag set for further actions
                if (lambda x, y: set(x).intersection(set(y)) != set())(new_hour, hour_table[1]):
                    self.flag.add(hour_table[0])
                    self.flag.add(index)
                    break
            time_table.append([index, new_hour])
        if not time_table:
            self.log.critical(f"Failed to generate time_table "
                              f"list and check is there is any duplicates "
                              f"{emoji.TASK_FAILED}")
        return time_table

    def get_flag(self):
        return self.flag
