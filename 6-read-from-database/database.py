"""
Fake database of employee data based on Corey Schafer's SQLite tutorial.
"""
import os
import sqlite3
from typing import Union
from pydantic import BaseModel


class Employee(BaseModel):
    """Basic employee information. """
    first: str
    last: str
    pay: int


class EmployeeDatabase:
    """Interface to `employees.db`."""
    _path: str = 'employees.db'

    def __init__(self, hard_reset: bool = False) -> None:
        if not os.path.isfile(self._path) or hard_reset:
            # create/clear `employees` table and reset ID increment counter
            with sqlite3.connect(self._path) as conn:
                cursor = conn.cursor()
                cursor.execute(
                    '''
                    CREATE TABLE IF NOT EXISTS employees (
                        employee_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        first TEXT NOT NULL,
                        last TEXT NOT NULL,
                        pay INTEGER NOT NULL
                    )
                    '''
                )
                cursor.execute('DELETE FROM employees')
                cursor.execute(
                    '''
                    DELETE FROM sqlite_sequence
                    WHERE name="employees"
                    '''
                )

            # seed `employees` table
            self.create(Employee(first='William', last='Zhang', pay=100_000))

    def create(self, employee: Employee) -> int:
        """Create a new entry in the `employees` table.

        Args:
            employee (Employee): employee information

        Returns:
            int: employee ID
        """
        with sqlite3.connect(self._path) as conn:
            cursor = conn.cursor()
            cursor.execute(
                '''
                INSERT INTO employees
                    (first, last, pay)
                VALUES
                    (:first, :last, :pay)
                ''',
                employee.dict()
            )
            insert_id = cursor.lastrowid
        return insert_id

    def readall(self) -> list:
        """Read every entry in the `employees` table.

        Returns:
            list: employee data
        """
        with sqlite3.connect(self._path) as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM employees')
            data = cursor.fetchall()
        return data

    def update(
        self,
        employee_id: int,
        column: str,
        value: Union[str, int]
    ) -> None:
        """UPDATE `employee` entry corresponding to an ID.

        Returns:
            employee_id (int): employee ID of entry to delete
            column (str): column to update
            value (Union[str, int]): new column value for employee
        """

        # sanitize <column> to defend against injection
        try:
            assert column in ['first', 'last', 'pay']
        except AssertionError:
            pass  # triage bad input, potential attack

        with sqlite3.connect(self._path) as conn:
            cursor = conn.cursor()
            cursor.execute(
                f'''
                UPDATE employees
                SET {column} = :value
                WHERE employee_id = :emp_id
                ''',
                {
                    'emp_id': employee_id,
                    'value': value
                }
            )

    def delete(self, employee_id: int) -> None:
        """Delete `employee` entry corresponding to an ID.

        Args:
            employee_id (int): employee ID of entry to delete
        """
        with sqlite3.connect(self._path) as conn:
            cursor = conn.cursor()
            cursor.execute(
                '''
                DELETE FROM employees
                WHERE employee_id = :emp_id
                ''',
                {'emp_id': employee_id}
            )
