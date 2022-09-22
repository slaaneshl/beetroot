from pprint import pprint
import sqlite3


def create_connect(path: str):
    connect = None
    try:
        connect = sqlite3.connect(path)
    except sqlite3.Error as e:
        print(f'sqlite connection error {e}')

    return connect


def execute_query(connect, query: str):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
    except sqlite3.Error as e:
        print(f'sqlite connection error {e}')


def select_query(connect, query: str):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except sqlite3.Error as e:
        print(f'sqlite connection error {e}')


connection = create_connect('hr_for_sql_lesson_35.db')

name_depart_for_each_employee = """
select employees.first_name || ' ' || employees.last_name || ', department: ' ||
 departments.depart_name || ', id: ' ||
 departments.department_id 
from employees
join departments using (department_id);
"""
name_depart_city_state_for_each_employee = """
select employees.first_name || ' ' || employees.last_name || ', department: ' ||
 departments.depart_name || ', city: ' || locations.city || ', state: ' || 
 locations.state_province 
from employees
join departments using (department_id)
join locations using (location_id);
"""
name_depart_for_80_or_40_employee = """
select employees.first_name || ' ' || employees.last_name || ', department: ' ||
 departments.depart_name || ', id: ' ||
 departments.department_id 
from employees
join departments on departments.department_id = employees.department_id
where departments.department_id in (80, 40);
"""
all_depart = """
select employees.first_name || ' ' || employees.last_name || ', id: ' ||
 departments.department_id || ', department: ' || departments.depart_name 
from employees
left join departments using (department_id);
"""
name_manager = """
select * from departments
"""
name_job_salary = """
select employees.first_name || ' ' || employees.last_name || ', job name: ' ||
 jobs.job_title || ', salary: ' || jobs.max_salary -  employees.salary
from jobs
join employees using (job_id);
"""
average_salary = """
select  'job: ' || jobs.job_title || ', average salary: ' || 
 AVG(employees.salary)
from employees 
join jobs using (job_id)
group by jobs.job_title order by AVG(employees.salary) desc
"""
location_london = """   
select first_name || ' ' || last_name AS Employee_name, salary
from employees 
join departments using (department_id) 
join  locations using (location_id) 
where locations.city = 'Southlake';
"""
# pprint(select_query(connection, name_depart_city_state_for_each_employee))
# pprint(select_query(connection, name_depart_for_80_or_40_employee))
# pprint(select_query(connection, all_depart))
# pprint(select_query(connection, name_manager))
# pprint(select_query(connection, name_job_salary))
pprint(select_query(connection, average_salary))
# pprint(select_query(connection, location_london))