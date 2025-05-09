"""
This class provides a simple interface to the different functionalities
of the Python SQLite module, to easily and quickly perform the various
operations on databases:

- create database
- connect, disconnect
- create and drop tables
- insert, update, select from tables
"""

from typing import Any
import os
import sqlite3

class Database:
    """
    This is the entry point to access Database features
    """

    def __init__(self, db_path: str) -> None:
        """
        Initialization of the Database object

        param db_path str contains the path to the database
        """
        self.status: dict[bool, str] = {"state": True, "message": "nil"}
        self.last_inserted_id: int = 0
        self.database: str = db_path
        self.connection: sqlite3.Connection = self.db_connect()
        self.cursor: sqlite3.Cursor | None = None
        if self.status:
            self.cursor = self.connection.cursor()

    def __del__(self):
        """Safely closing the connection when going out of scope"""
        self.db_close()

    def db_connect(self) -> sqlite3.Connection | None:
        """
        Operates connection to the database

        return bool True on succes, False on failure to connect to the daatabase
        """
        con: sqlite3.Connection | None = None
        try:
            con = sqlite3.connect(self.database)
        except (sqlite3.OperationalError, sqlite3.Error) as ex:
            self.status["state"] =  False
            self.status["message"] =  f"\033[91mError:\033[0m {ex}"

        return con

    def db_close(self) -> None:
        """
        This method is responsible for closing the connection to the database
        """
        try:
            if self.status:
                self.connection.close()
        except (sqlite3.OperationalError, sqlite3.Error) as ex:
            self.status["state"] =  False
            self.status["message"] =  f"\033[91mError:\033[0m {ex}"

    def db_count(self, table_name: str, conditions: str|None = None) -> int:
        """Simply getting the total number of rows in any table"""
        res: int = 0
        query = f"SELECT COUNT(*) FROM {table_name}"
        if conditons is not None:
            query += f" {conditions}"
        self.cursor.execute(query)
        row_count = self.cursor.fetchone()
        res = row_count[0]
        return res

    def db_read(self, query: str, params: tuple[Any], single_row: bool = True) -> Any:
        """
        Execute a query on the database
        """
        '''
        # This is the qmark style used in a SELECT query:
        params = (1972,)
        cur.execute("SELECT * FROM lang WHERE first_appeared = ?", params)
        print(cur.fetchall())
        '''
        result: Any = None

        try:
            result = self.cursor.execute(query, params)
            if single_row:
                result.fetchone()
            else:
                result.fetchall()
        except (sqlite3.OperationalError, sqlite3.Error) as ex:
            self.status["state"] =  False
            self.status["message"] =  f"\033[91mError:\033[0m {ex}"
            result = None

        return result

    def db_write(self, query: str, data: dict[str, Any], insert: bool, single_row: bool = True) -> None:
        """
        Execute a query on the database
        """
        '''
        # This is the named style used with executemany():
        data = (
            {"name": "C", "year": 1972},
            {"name": "Fortran", "year": 1957},
            {"name": "Python", "year": 1991},
            {"name": "Go", "year": 2009},
        )

        executemany("INSERT INTO table VALUES(:name, :year)", data)
        '''
        try:
            if single_row:
                self.cursor.execute(query, data)
                if insert:
                    self.last_inserted_id = self.cursor.lastrowid
            else:
                self.executemany(query, data)

        except (sqlite3.OperationalError, sqlite3.Error) as ex:
            self.status["state"] =  False
            self.status["message"] =  f"\033[91mError:\033[0m {ex}"

        self.connection.commit()

