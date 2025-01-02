"""
CRUD interface for employee database.
"""
from typing import Union
from fastapi import FastAPI
import database


app = FastAPI()
app_db = database.EmployeeDatabase(hard_reset=True)


@app.post('/new/')
async def create(employee: database.Employee) -> dict:
    """CREATE a new employee record in database.

    Args:
        employee (database.Employee): employee information

    Returns:
        dict: new employee ID
    """
    employee_id = app_db.create(employee)
    return {'employee_id': employee_id}


@app.get('/getall/')
async def readall() -> list:
    """READ all employees in the database.

    Returns:
        list: employee data
    """
    return app_db.readall()


@app.patch('/update/{employee_id}/{column}/{value}')
async def update(
    employee_id: int,
    column: str,
    value: Union[str, int]
) -> None:
    """UPDATE `employee` entry corresponding to an ID.

    Returns:
        employee_id (int): employee ID of entry to delete
        column (str): column to update
        value (Any): new column value for employee
    """
    app_db.update(employee_id, column, value)


@app.delete('/delete/{employee_id}')
async def delete(employee_id: int) -> None:
    """DELETE `employee` entry corresponding to an ID.

    Args:
        employee_id (int): employee ID of entry to delete
    """
    app_db.delete(employee_id)
