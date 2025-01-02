"""
CRUD interface for employee database.
"""
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
