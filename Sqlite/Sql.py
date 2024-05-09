import sqlite3 as db
from Employee import Employee
from tabulate import tabulate

#connection
conn = db.connect('my_database.db')

c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS Employee(
          fname  text,
          lname  text,
          pay   integer)''')

def insert_emp(emp):
    with conn:
        c.execute('INSERT INTO Employee VALUES(:fname,:lname,:pay)'
                  ,{'fname':emp.fname,'lname':emp.lname,'pay':emp.pay})

def get_emp_by_lname(lname):
    c.execute('SELECT * FROM Employee WHERE lname = :lname',({'lname':lname}))
    return c.fetchall()


def get_all_lname():
    c.execute('SELECT * FROM Employee')
    return c.fetchall()

def update_pay(emp,pay):
    with conn:
        c.execute('UPDATE Employee SET pay =:pay WHERE fname = :fname AND lname = :lname',
                  {'fname':emp.fname,'lname':emp.lname,'pay':pay})

def remove_emp(emp):
    with conn:
        c.execute('DELETE from Employee WHERE fname = :fname AND lname =:lname',
                  {'fname':emp.fname,'lname':emp.lname})

emp_1 = Employee('Mahdi','Shabani',200)
emp_2 = Employee('Ali','Sams',300)
emp_3 = Employee('Reza','Golzar',400)
emp_4 = Employee('Rambod','Javan',500)

#insert_emp(emp_1)
#insert_emp(emp_2)
#insert_emp(emp_3)
#insert_emp(emp_4)

#remove_emp(emp_4)
emps = get_emp_by_lname('Sams')
print(emps)


conn.close()