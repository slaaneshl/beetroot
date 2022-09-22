import sqlite3
from sqlite3 import Error


def create_connect(path: str):
    connect = None

    try:
        connect = sqlite3.connect(path)

    except Error:
        print(f'sqlite3 connection error {Error}')

    return connect


def execute_query(connect, query: str):
    cursor = connection.cursor()

    try:
        cursor.execute(query)
        connect.commit()

    except Error:
        print(f'sqlite3 connection error {Error}')


connection = create_connect('lesson_34_sql.sqlite')

create_employees_table = """
CREATE TABLE employees (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    language TEXT,
    age INTEGER NOT NULL,
    experience_years INTEGER NOT NULL
);
"""
create_task_table = """
CREATE TABLE tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    deadline TEXT,
    employee_id INTEGER NOT NULL,
    FOREIGN KEY (employee_id) REFERENCES employees (id)
);
"""

create_competed_tasks_table = """
CREATE TABLE completed_tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    time_to_done INTEGER NOT NULL,
    employee_id INTEGER NOT NULL,
    task_id INTEGER NOT NULL,
    FOREIGN KEY (employee_id) REFERENCES employees (id),
    FOREIGN KEY (task_id) REFERENCES tasks (id),
    FOREIGN KEY (title) REFERENCES tasks (title)
);
"""

create_best_employees_table = """
CREATE TABLE best_emp (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    employee_id INTEGER NOT NULL,
    FOREIGN KEY (employee_id) REFERENCES employees (id)
);
"""

# execute_query(connection, create_employees_table)
# execute_query(connection, create_task_table)
# execute_query(connection, create_competed_tasks_table)
# execute_query(connection, create_best_employees_table)

create_employees = """
INSERT INTO
    employees (name, language, age, experience_years)
VALUES 
    ('Alex', 'English/Ukraine', 21, 4),
    ('Lev', 'English/Ukraine', 19, 1),
    ('Hitoshi', 'English/Japanese', 51, 11),
    ('Jack', 'English', 25, 6),
    ('Oleg', 'English/Ukraine', 31, 1);
"""

create_task = """
INSERT INTO 
    tasks (title, deadline, employee_id)
VALUES
    ('Math task with calculator', '11.10', 2),
    ('Install Python 3.01', '02.10', 2),
    ('Write "Hello world!" on Python', '05.10', 5),
    ('Finish database', '22.10', 3),
    ('Teach juniors "2 + 2"', '03.10', 3),
    ('Create new plan how to pay more for our employees', '14.10', 4),
    ('Check all task for all employees', '29.10', 1);
"""

create_competed_tasks = """
INSERT INTO 
    completed_tasks (title, time_to_done, employee_id, task_id) 
VALUES 
    ('Teach juniors "2 + 2"', 15, 3, 5),
    ('Install Python 3.01', 14, 2, 2);
"""
create_best_employees = """
INSERT INTO
    best_emp (name, employee_id) 
VALUES 
    ('Oleg', 5),
    ('Hitoshi', 3);
"""
# execute_query(connection, create_employees)
# execute_query(connection, create_task)
# execute_query(connection, create_competed_tasks)
# execute_query(connection, create_best_employees)

# rename_table = """
# ALTER TABLE best_emp
# RENAME TO favorite_employees;
# """

add_new_column = """
ALTER TABLE employees
ADD COLUMN location;
"""

# execute_query(connection, add_new_column)

update_column_value = """
UPDATE employees
SET location = 'Chernivsti'
WHERE id = 2;
"""
# execute_query(connection, update_column_value)

delete_column_value = """
DELETE FROM employees
WHERE id = 5;
"""
# execute_query(connection, delete_column_value)
