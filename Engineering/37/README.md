
# SQLAlchemy

***It is the SQL Toolkit for Python and also Python's ORM enabler***

#### Features

- Supports dialect for SLQLite, Postgres, MySQL, Oracle, SQLServer, etc.
- Allow you to interact with RDBMS with standard SQL.
- Allow object based interaction with RDBMS (ORM - Object Relational Mapping).

***Advantage & Disadvantage of using SQL & ORM***

|SQL|ORM|
|---|---|
|More flexible|More Pythonic|
|Have performance advantage in some cases|It is safe and less error prone|
|Make use of RDMS specific optimization/syntax|It allow code to be generic and portable across RDBMS|


#### RDBMS Instance

As this is all about RDBMS we need a running RDBMS, in our case we have MySQL.

- Let's confirm we have one running.

```commandline
[root@localhost ~]# mysql -u root -pAdmin@123
mysql: [Warning] Using a password on the command line interface can be insecure.
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 15
Server version: 8.0.26 Source distribution

Copyright (c) 2000, 2021, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql> exit
Bye
```

- Lets understand a schema

  `SCHEMA DETAIL`: We consider a simple cars database for which you can find the ER Diagram [LINK](MySQL-Sample-Database-Diagram-PDF-A4.pdf).

> The databse name is `classicmodels`.

```commandline
mysql> use classicmodels;
Database changed
mysql> show tables;
+-------------------------+
| Tables_in_classicmodels |
+-------------------------+
| customers               |
| employees               |
| offices                 |
| orderdetails            |
| orders                  |
| payments                |
| productlines            |
| products                |
+-------------------------+
8 rows in set (0.01 sec)

mysql> CREATE USER 'rpython'@'%' IDENTIFIED BY 'Password-123';
Query OK, 0 rows affected (0.02 sec)

mysql> GRANT ALL PRIVILEGES ON *.* TO 'rpython'@'%' WITH GRANT OPTION;
Query OK, 0 rows affected (0.01 sec)

```

#### Install SQLAlchemy

- You should be able to install SQLAlchemy using pip as below.

```commandline
pip install sqlalchemy
```

- Also, you need to install connector which is specific to the database we choose in our case it is MySQL.

```commandline
pip install mysql-connector-python
```

> Note, this is a pure Python connector.


#### Connection and REPL Test

```python
import sqlalchemy as db
engine = db.create_engine("mysql+mysqlconnector://rpython:Password-123@192.168.56.101:3306/classicmodels")
conn = engine.connect()

res = engine.execute("select * from customers limit 10")

type(res.fetchone())
# <class 'sqlalchemy.engine.row.LegacyRow'>
type(res.fetchone().items())
#<class 'list'>

print(res.fetchone())
# (103, 'Atelier graphique', 'Schmitt', 'Carine ', '40.32.2555', '54, rue Royale', None, 'Nantes', None, '44000', 'France', 1370, Decimal('21000.00'))

res.fetchmany(5)
#[(121, 'Baane Mini Imports', 'Bergulfsen', 'Jonas ', '07-98 9555', 'Erling Skakkes gate 78', None, 'Stavern', None, '4110', 'Norway', 1504, Decimal('81700.00')), (124, 'Mini Gifts Distributors Ltd.', 'Nelson', 'Susan', '4155551450', '5677 Strong St.', None, 'San Rafael', 'CA', '97562', 'USA', 1165, Decimal('210500.00')), (125, 'Havel & Zbyszek Co', 'Piestrzeniewicz', 'Zbyszek ', '(26) 642-7555', 'ul. Filtrowa 68', None, 'Warszawa', None, '01-012', 'Poland', None, Decimal('0.00')), (128, 'Blauer See Auto, Co.', 'Keitel', 'Roland', '+49 69 66 90 2555', 'Lyonerstr. 34', None, 'Frankfurt', None, '60528', 'Germany', 1504, Decimal('59700.00')), (129, 'Mini Wheels Co.', 'Murphy', 'Julie', '6505555787', '5557 North Pendale Street', None, 'San Francisco', 'CA', '94217', 'USA', 1165, Decimal('64600.00'))]

len(res.fetchall())
1
```

***NOTE:***

- Some special character in `Connection String` need to be URL Encoded, e.g. ( `@` as %40 ) 
- Note the result set is an `Cursor` and that's why above `fetchall` returned only 1


#### Panda and SQLAlchemy

You can work with data in RDBMS using Pandas by below method.

```commandline
>> import sqlalchemy as db
>> engine = db.create_engine("mysql+mysqlconnector://rpython:Password-123@192.168.56.101:3306/classicmodels")
>> conn = engine.connect()
>> import pandas as pd
>> qry = "select * from employees limit 100"
>> emp_df = pd.read_sql_query(db.text(qry), conn)

>> type(emp_df)
<class 'pandas.core.frame.DataFrame'>

>> emp_df.columns
Index(['employeeNumber', 'lastName', 'firstName', 'extension', 'email',
       'officeCode', 'reportsTo', 'jobTitle'],
      dtype='object')

>> emp_df.dtypes
employeeNumber      int64
lastName           object
firstName          object
extension          object
email              object
officeCode         object
reportsTo         float64
jobTitle           object
dtype: object

>> emp_df.count()
employeeNumber    23
lastName          23
firstName         23
extension         23
email             23
officeCode        23
reportsTo         22
jobTitle          23
dtype: int64

>> emp_df.head()
   employeeNumber   lastName  ... reportsTo              jobTitle
0            1002     Murphy  ...       NaN             President
1            1056  Patterson  ...    1002.0              VP Sales
2            1076   Firrelli  ...    1002.0          VP Marketing
3            1088  Patterson  ...    1056.0  Sales Manager (APAC)
4            1102     Bondur  ...    1056.0   Sale Manager (EMEA)
[5 rows x 8 columns]

>> emp_df.describe()
       employeeNumber    reportsTo
count       23.000000    22.000000
mean      1335.391304  1117.409091
std        223.565475   120.173549
min       1002.000000  1002.000000
25%       1154.000000  1064.000000
50%       1323.000000  1102.000000
75%       1557.500000  1143.000000
max       1702.000000  1621.000000
```

#### Object Relational Mapper

- Basically it allows `conversion of object between incompatible type` systems applicable in Object Oriented Programming.

- Below are major components:
  - Table: RDBMS table representation.
  - Mapper: Mapping between Python class and a RDBMS table.
  - Class: Definition of record map to an object.

- There are two type of mapping technique as discussed below:

  - Classical Mapping: Mapper function defines the mapping logic. This is not the de-facto standard thus not waste time in it.
  - Declarative Mapping: Session object based where Class declared with one to one mapping to RDBMS table.


***Declarative Mapping***

- `Session` are the entry point for RDBMS to Python communication via SQLAlchemy. It also wraps transaction.

```python
from sqlalchemy.orm import sessionmaker
ssn = sessionmaker()
ssn.configure(bind=engine) # Here engine is an SQLAlchemy engine
session = ssn()
```

> Note the best way to create manage session is as ContextManager.

```python
from sqlalchemy.orm import sessionmaker
import sqlalchemy import create_engine
session_maker = sessionmaker(bind=create_engine("mysql+mysqlconnector://rpython:Password-123@192.168.56.101:3306/classicmodels"))
with session_maker() as session:
    # Do your work with session
```

- `Declarative Base` is the base class for declarative class definition or the `Model`. Basically you need to define this and make all your Model (RDBMS Table) class definition inherit this.

```python
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()
```

- `Create Database` is a very RDBMS specific operation thus you need to use SQL approach and SQL dialect should be correct for specific RDBMS.

> Note for SQLLite RDBMS you so not need to run any SQL, connect string (sqllite3:///[DB FILE]) will open a new database ***file*** if already does not exist.

```python
import sys
sys.path.append('C:/Users/HP/OneDrive/Desktop/work/PythonCheatsheet/Engineering/37')
import sqlalchemy_eg_01 as sa

eng_t = sa.get_engine()
conn_t = sa.get_connection(eng_t)
sa.create_db(conn_t, "tmp_db")

sa.create_db(conn_t, "tmp_db")
```

> For creating database you can see the [code](./sqlalchemy_eg_01.py) the connection string does not contain database parameter.


- `Create Tables` are basically means defining class with columns with type and constrain (primary and foreign keys) attributes. Once done you should ask sessions metadata object to create all staged metadata.


```python
eng = sa.get_engine("tmp_db")
conn = sa.get_connection(eng)
sa.create_all_objects(eng)

import sqlalchemy as db
conn.execute(db.text("show tables")).fetchall()
#[('employees',), ('offices',)]
```

- `Updatable` table definition

In case you want a table that need to be updated in the future, e.g. add, drop column, etc. Use below setting.

```python
class SomeTable(Base):
    """Example Table Model"""
    __tablename__ = 'sometable'
    __table_args__ = {'extend_existing': True}
    dummy_column = db.Column(db.Integer(), primary_key=True)
```

> Like extend_existing there are other options, check [LINK](https://martinheinz.dev/blog/28) for good read on this.

- `Table Relationship` is handled by relationship class.


  - `One-to-many` Relationship: In SQLAlchemy, one-to-many relationships are defined using a Foreign Key on the many side of the relationship, which points to the primary key of the one side.

```python
class Customer(Base):
    __tablename__ = 'customer'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    orders = relationship("Order", back_populates="customer")

class Order(Base):
    __tablename__ = 'order'
    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey('customer.id'))
    customer = relationship("Customer", back_populates="orders")
```

***Usage***

```python
customer = session.query(Customer).get(1)
order = Order(customer=customer)
session.add(order)
session.commit()

customer = session.query(Customer).get(1)
orders = customer.orders
```

  - `Many-to-one` Relationship: Defined using a Foreign Key on the many side of the relationship, which points to the primary key of the one side.

```python
class Customer(Base):
    __tablename__ = 'customer'
    id = Column(Integer, primary_key=True)
    name = Column(String)

class Order(Base):
    __tablename__ = 'order'
    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey('customer.id'))
    customer = relationship("Customer")
```

  - `Many-to-many` Relationship: Implemented using an intermediate table, also known as an association table, that maps the relationships between the two entities.

```python
class Student(Base):
    __tablename__ = 'student'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    courses = relationship("Course", secondary="student_course", back_populates="students")

class Course(Base):
    __tablename__ = 'course'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    students = relationship("Student", secondary="student_course", back_populates="courses")

class StudentCourse(Base):
    __tablename__ = 'student_course'
    student_id = Column(Integer, ForeignKey('student.id'), primary_key=True)
    course_id = Column(Integer, ForeignKey('course.id'), primary_key=True)
```

- `Insert record(s)` can be achieved by simply create table objects and asking session to persist them by adding to session and then committing the session.

  - Single record can be added as below.
  
```python
ofc01 = sa.Offices(office_name="ACN", office_city="Kolkata", office_country="India")
session = sa.get_session(eng)
sa.add_single_object_in_session(session, ofc01)
sa.check_uncommited_object(session)
#IdentitySet([<sqlalchemy_eg_01.Offices object at 0x000001776C35F520>])
sa.commit_session(session)
```

  - Verify result.

```commandline
mysql> select * from offices;
+-----------+-------------+-------------+----------------+-----------------+
| office_id | office_name | office_city | office_country | office_strength |
+-----------+-------------+-------------+----------------+-----------------+
|         1 | ACN         | Kolkata     | India          |            1000 |
+-----------+-------------+-------------+----------------+-----------------+
1 row in set (0.00 sec)

```

  - Insert multiple records.

```python
session.rollback()
emp01 = sa.Employees(emp_name="Sankar", emp_phone=456789, emp_office=1)
emp02 = sa.Employees(emp_name="Dabli", emp_phone=4506777, emp_office=1)
sa.check_uncommited_object(session)
IdentitySet([])
sa.add_multiple_object_in_session(session, [emp01, emp02])
sa.check_uncommited_object(session)
IdentitySet([<sqlalchemy_eg_01.Employees object at 0x000001776C3B2C10>, <sqlalchemy_eg_01.Employees object at 0x000001776C3B2AC0>])
sa.commit_session(session)
```

> Note at any point if there is exception thrown, or you want to clear the staged work in session, you can perform a `rollback`.

  - Verify results.

```commandline
mysql> select * from employees;
+--------+----------+-----------+------------+
| emp_id | emp_name | emp_phone | emp_office |
+--------+----------+-----------+------------+
|      2 | Sankar   |    456789 |          1 |
|      3 | Dabli    |   4506777 |          1 |
+--------+----------+-----------+------------+
2 rows in set (0.00 sec)
```

- `Bulk Load` csv (or any other format file) with Pandas.

  - Check file to load.

```commandline
PS C:\Users\HP\OneDrive\Desktop\work\PythonCheatsheet> cat .\Engineering\37\sample_offices.csv
office_id,office_name,office_city,office_country,office_strength
2,HCL,Noida,India,6000
3,TCS,Mumbai,India,9000
4,IBM,NYC,USA,2500
```

  - Open file in Python and read as Pandas dataframe.

```python
import pandas as pd
with open('Engineering/37/sample_offices.csv', 'r') as f:
    off_df = pd.read_csv(f)
    
off_df.head()
   office_id office_name office_city office_country  office_strength
0          2         HCL       Noida          India             6000
1          3         TCS      Mumbai          India             9000
2          4         IBM         NYC            USA             2500
```

  - Persist in RDBMS.

```python
import sys
sys.path.append('C:/Users/HP/OneDrive/Desktop/work/PythonCheatsheet/Engineering/37')
import sqlalchemy_eg_01 as sa

eng_t = sa.get_engine("tmp_db")
conn_t = sa.get_connection(eng_t)

import pandas as pd
with open('Engineering/37/sample_offices.csv', 'r') as f:
    off_df = pd.read_csv(f)
    
off_df.head()
   office_id office_name office_city office_country  office_strength
0          2         HCL       Noida          India             6000
1          3         TCS      Mumbai          India             9000
2          4         IBM         NYC            USA             2500
off_df.to_sql('offices_new', con=conn_t)
3
conn_t.commit()

```

> Note you cannot append to an existing table.

  - Verify result.

```commandline
mysql> select * from offices_new;
+-------+-----------+-------------+-------------+----------------+-----------------+
| index | office_id | office_name | office_city | office_country | office_strength |
+-------+-----------+-------------+-------------+----------------+-----------------+
|     0 |         2 | HCL         | Noida       | India          |            6000 |
|     1 |         3 | TCS         | Mumbai      | India          |            9000 |
|     2 |         4 | IBM         | NYC         | USA            |            2500 |
+-------+-----------+-------------+-------------+----------------+-----------------+
3 rows in set (0.00 sec)
```

- `Query` objects from RDBMS

  - Executing standard query via SQLAlchemy

```commandline
mysql> select emp_name from employees where emp_name like '%i%';
+----------+
| emp_name |
+----------+
| Dabli    |
| Alif     |
+----------+
2 rows in set (0.01 sec)
```

  - Use connection to execute query

```python
from sqlalchemy import text
qry_str = """select emp_name from employees where emp_name like '%i%'"""
conn_t.execute(text(qry_str)).fetchall()
[('Dabli',), ('Alif',)]
```

  - Declarative ORM

    - Build session (connection between Python and RDBMS and entry point for query)

```python
from sqlalchemy.orm import sessionmaker
ssn = sessionmaker()
ssn.configure(bind=eng_t)
c_ssn = ssn()
``` 

    - Query table data

```python
c_ssn.query(sa.Employees).all()
[<sqlalchemy_eg_01.Employees object at 0x0000016E91E73880>, <sqlalchemy_eg_01.Employees object at 0x0000016E91E73100>, <sqlalchemy_eg_01.Employees object at 0x0000016E91E73A30>, <sqlalchemy_eg_01.Employees object at 0x0000016E91E739A0>]
[ e.emp_name for e in c_ssn.query(sa.Employees).all() ]
['Sankar', 'Dabli', 'Alif', 'Jewel']

c_ssn.query(sa.Employees).first().emp_name
'Sankar'

type(c_ssn.query(sa.Employees.emp_name))
<class 'sqlalchemy.orm.query.Query'>
print(c_ssn.query(sa.Employees.emp_name))
SELECT employees.emp_name AS employees_emp_name 
FROM employees

c_ssn.query(sa.Employees.emp_name, sa.Employees.emp_office).first()
('Sankar', 3)
```

> Note with `echo` parameter set during engine creation you can print all SQL executed by SQLAlchemy.

  - Complex Query

```python
len(c_ssn.query(sa.Employees).filter_by(emp_office=2).all())
1
c_ssn.query(sa.Employees).filter_by(emp_office=2).first().emp_name
'Jewel'

c_ssn.query(sa.Employees).filter(sa.Employees.emp_office==2).first().emp_name
'Jewel'

[ e.emp_name for e in c_ssn.query(sa.Employees).filter(sa.Employees.emp_name.like('%i%')).all() ]
['Dabli', 'Alif']

[ e.emp_name for e in c_ssn.query(sa.Employees).filter(sa.Employees.emp_name.like('%l%'), sa.Employees.emp_office==2).all() ]
['Jewel']
from sqlalchemy import or_
[ e.emp_name for e in c_ssn.query(sa.Employees).filter(or_(sa.Employees.emp_name.like('%l%'), sa.Employees.emp_office==2)).all() ]
['Dabli', 'Alif', 'Jewel']
```

> Note the difference between `filter` and `filter_by`, one allow column resolution. Also note the way logical `OR` is used.


  - SQLAlchemy functions

```python
from sqlalchemy import func

print(c_ssn.query(func.lower(sa.Employees.emp_name)).first())
('sankar',)

c_ssn.query(func.max(sa.Employees.emp_phone)).scalar()
4506777

c_ssn.query(sa.Offices.office_name, (sa.Offices.office_strength - 100).label('Updated Strength')).limit(1).all()
[('ACN', 900)]

c_ssn.query(sa.Offices.office_name, (sa.Offices.office_strength - 100).label('Updated Strength')).order_by('Updated Strength').limit(1).all()
[('ACN', 900)]

from sqlalchemy import desc
c_ssn.query(sa.Offices.office_name, (sa.Offices.office_strength - 100).label('Updated Strength')).order_by(desc('Updated Strength')).limit(1).all()
[('ACN', 900)]

from sqlalchemy import cast
from sqlalchemy import cast, String
c_ssn.query(sa.Offices.office_name, cast((sa.Offices.office_strength - 100), String).label('Updated Strength')).limit(1).all()
[('ACN', '900')]
```

> Note `scalar` allows you to extract a single value returned also how we can explicitly `cast` result.


  - Joins

```python
for emp_off in c_ssn.query(sa.Employees, sa.Offices).join(sa.Offices, sa.Employees.emp_office == sa.Offices.office_id).all():
    print("{} - {}".format(emp_off[0].emp_name, emp_off[1].office_name))
    
Sankar - CTS
Dabli - CTS
Alif - CTS
Jewel - ACN

for emp_off in c_ssn.query(sa.Employees, sa.Offices).filter(sa.Employees.emp_office == sa.Offices.office_id).all():
    print("{} - {}".format(emp_off[0].emp_name, emp_off[1].office_name))
    
Sankar - CTS
Dabli - CTS
Alif - CTS
Jewel - ACN
```

> Note above the former is called `Explicit` join and later `Implicit` join.

  - Hierarchical Tables & Self Joins

> Define a Hierarchical table

```python
importlib.reload(sa)
<module 'sqlalchemy_eg_01' from 'C:/Users/HP/OneDrive/Desktop/work/PythonCheatsheet/Engineering/37\\sqlalchemy_eg_01.py'>
sa.create_all_objects(eng_t)
sa.add_multiple_object_in_session(session, [mn01, mn02])
sa.commit_session(session)
mn03 = sa.Managers(emp_name="Alif", emp_manager=1)
mn04 = sa.Managers(emp_name="Dabli", emp_manager=2)
sa.add_multiple_object_in_session(session, [mn03, mn04])
sa.commit_session(session)
```

> Query Hierarchical table

```python
from sqlalchemy.orm import aliased
Reporte = aliased(sa.Managers)

session.query(sa.Managers.emp_name, Reporte.emp_name).filter(sa.Managers.emp_id == Reporte.emp_manager).all()
[('Jewel', 'Alif'), ('Amitav', 'Dabli')]
```

> Note above the way to perform `Projection` in SQLAlchemy, by only having fields required in Query dataset.


- `Update` object in RDBMS

  - Before


```commandline
mysql> select * from managers;
+--------+----------+-------------+
| emp_id | emp_name | emp_manager |
+--------+----------+-------------+
|      1 | Jewel    |        NULL |
|      2 | Amitav   |        NULL |
|      3 | Alif     |           1 |
|      4 | Dabli    |           2 |
+--------+----------+-------------+
4 rows in set (0.00 sec)
```


```python
engine = db.create_engine("mysql+mysqlconnector://rpython:Password-123@192.168.56.101:3306/tmp_db")
conn = engine.connect()
ssn = sessionmaker()
ssn.configure(bind=engine)
session = ssn()
session.query(sa.Managers).filter(sa.Managers.emp_name == 'Dabli').update({sa.Managers.emp_manager: 1}, synchronize_session = False)
1
session.commit()

```


  - Result


```commandline
mysql> select * from managers;
+--------+----------+-------------+
| emp_id | emp_name | emp_manager |
+--------+----------+-------------+
|      1 | Jewel    |        NULL |
|      2 | Amitav   |        NULL |
|      3 | Alif     |           1 |
|      4 | Dabli    |           1 |
+--------+----------+-------------+
4 rows in set (0.00 sec)
```

- `Delete` record in RDBMS

```python
unused_manager = session.query(sa.Managers).filter(sa.Managers.emp_id == 2).first()
unused_manager.emp_name
'Amitav'
session.delete(unused_manager)
session.commit()

session.query(sa.Managers).filter(sa.Managers.emp_id == 4).delete()
1
session.commit()

```

  - Result

```commandline
mysql> select * from managers;
+--------+----------+-------------+
| emp_id | emp_name | emp_manager |
+--------+----------+-------------+
|      1 | Jewel    |        NULL |
|      3 | Alif     |           1 |
+--------+----------+-------------+
2 rows in set (0.00 sec)

```

- `Metadata Catalog` access

```python
metastore = db.MetaData()
metastore.reflect(bind=engine)

metastore.tables.keys()
dict_keys(['employees', 'offices', 'managers', 'offices_new'])

metastore.tables.items()
dict_items([('employees', Table('employees', MetaData(), Column('emp_id', INTEGER(), table=<employees>, primary_key=True, nullable=False), Column('emp_name', VARCHAR(length=50), table=<employees>, nullable=False), Column('emp_phone', INTEGER(), table=<employees>), Column('emp_office', INTEGER(), ForeignKey('offices.office_id'), table=<employees>, nullable=False), schema=None)), ('offices', Table('offices', MetaData(), Column('office_id', INTEGER(), table=<offices>, primary_key=True, nullable=False), Column('office_name', VARCHAR(length=50), table=<offices>, nullable=False), Column('office_city', VARCHAR(length=15), table=<offices>, nullable=False), Column('office_country', VARCHAR(length=15), table=<offices>, nullable=False), Column('office_strength', INTEGER(), table=<offices>), schema=None)), ('managers', Table('managers', MetaData(), Column('emp_id', INTEGER(), table=<managers>, primary_key=True, nullable=False), Column('emp_name', VARCHAR(length=50), table=<managers>, nullable=False), Column('emp_manager', INTEGER(), table=<managers>), schema=None)), ('offices_new', Table('offices_new', MetaData(), Column('index', BIGINT(), table=<offices_new>), Column('office_id', BIGINT(), table=<offices_new>), Column('office_name', TEXT(), table=<offices_new>), Column('office_city', TEXT(), table=<offices_new>), Column('office_country', TEXT(), table=<offices_new>), Column('office_strength', BIGINT(), table=<offices_new>), schema=None))])

metastore.tables.values()
dict_values([Table('employees', MetaData(), Column('emp_id', INTEGER(), table=<employees>, primary_key=True, nullable=False), Column('emp_name', VARCHAR(length=50), table=<employees>, nullable=False), Column('emp_phone', INTEGER(), table=<employees>), Column('emp_office', INTEGER(), ForeignKey('offices.office_id'), table=<employees>, nullable=False), schema=None), Table('offices', MetaData(), Column('office_id', INTEGER(), table=<offices>, primary_key=True, nullable=False), Column('office_name', VARCHAR(length=50), table=<offices>, nullable=False), Column('office_city', VARCHAR(length=15), table=<offices>, nullable=False), Column('office_country', VARCHAR(length=15), table=<offices>, nullable=False), Column('office_strength', INTEGER(), table=<offices>), schema=None), Table('managers', MetaData(), Column('emp_id', INTEGER(), table=<managers>, primary_key=True, nullable=False), Column('emp_name', VARCHAR(length=50), table=<managers>, nullable=False), Column('emp_manager', INTEGER(), table=<managers>), schema=None), Table('offices_new', MetaData(), Column('index', BIGINT(), table=<offices_new>), Column('office_id', BIGINT(), table=<offices_new>), Column('office_name', TEXT(), table=<offices_new>), Column('office_city', TEXT(), table=<offices_new>), Column('office_country', TEXT(), table=<offices_new>), Column('office_strength', BIGINT(), table=<offices_new>), schema=None)])

table_object = metastore.tables['employees']
table_object.columns.values()
[Column('emp_id', INTEGER(), table=<employees>, primary_key=True, nullable=False), Column('emp_name', VARCHAR(length=50), table=<employees>, nullable=False), Column('emp_phone', INTEGER(), table=<employees>), Column('emp_office', INTEGER(), ForeignKey('offices.office_id'), table=<employees>, nullable=False)]

```

- `Drop` table

```python
table_object = metastore.tables['offices_new']
table_object.drop(bind=engine)
session.commit()
```

  - Result
  
```commandline
mysql> show tables;
+------------------+
| Tables_in_tmp_db |
+------------------+
| employees        |
| managers         |
| offices          |
+------------------+
3 rows in set (0.00 sec)
```


- `Migration` with Alembic

DB Migration helps in managing database for a project in a more structured and error free fashion. SQLAlchemy out of the box lacks support for migration for which we need a library called Alembic.

  - Get [Alembic](https://alembic.sqlalchemy.org/en/latest/)
  
```commandline
pip install -r requirements.txt
```

  - Setup project

```commandline
Hewlett Packard@HP-Elitedesk-PC MINGW64 ~/OneDrive/Desktop/work/PythonCheatsheet/Engineering/37/db-migartion (37)
$ ls -ltr
total 1
drwxr-xr-x 1 Hewlett Packard 197121   0 Mar 19 13:28 37venv/
-rw-r--r-- 1 Hewlett Packard 197121 181 Mar 19 13:34 requirements.txt

(37venv)
Hewlett Packard@HP-Elitedesk-PC MINGW64 ~/OneDrive/Desktop/work/PythonCheatsheet/Engineering/37/db-migartion (37)
$ alembic.exe init db_migration
Creating directory C:\Users\HP\OneDrive\Desktop\work\PythonCheatsheet\Engineering\37\db-migartion\db_migration ...  done
Creating directory C:\Users\HP\OneDrive\Desktop\work\PythonCheatsheet\Engineering\37\db-migartion\db_migration\versions ...  done
Generating C:\Users\HP\OneDrive\Desktop\work\PythonCheatsheet\Engineering\37\db-migartion\alembic.ini ...  done
Generating C:\Users\HP\OneDrive\Desktop\work\PythonCheatsheet\Engineering\37\db-migartion\db_migration\env.py ...  done
Generating C:\Users\HP\OneDrive\Desktop\work\PythonCheatsheet\Engineering\37\db-migartion\db_migration\README ...  done
Generating C:\Users\HP\OneDrive\Desktop\work\PythonCheatsheet\Engineering\37\db-migartion\db_migration\script.py.mako ...  done
Please edit configuration/connection/logging settings in 'C:\\Users\\HP\\OneDrive\\Desktop\\work\\PythonCheatsheet\\Engineering\\37\\db-migartion\\alembic.ini' before proceeding.

(37venv)
Hewlett Packard@HP-Elitedesk-PC MINGW64 ~/OneDrive/Desktop/work/PythonCheatsheet/Engineering/37/db-migartion (37)
$ ls -ltr
total 5
drwxr-xr-x 1 Hewlett Packard 197121    0 Mar 19 13:28 37venv/
-rw-r--r-- 1 Hewlett Packard 197121  181 Mar 19 13:34 requirements.txt
-rw-r--r-- 1 Hewlett Packard 197121 3388 Mar 19 13:37 alembic.ini
drwxr-xr-x 1 Hewlett Packard 197121    0 Mar 19 13:37 db_migration/
(37venv)
Hewlett Packard@HP-Elitedesk-PC MINGW64 ~/OneDrive/Desktop/work/PythonCheatsheet/Engineering/37/db-migartion (37)
$ ls -ltr db_migration/
total 9
drwxr-xr-x 1 Hewlett Packard 197121    0 Mar 19 13:37 versions/
-rw-r--r-- 1 Hewlett Packard 197121 2103 Mar 19 13:37 env.py
-rw-r--r-- 1 Hewlett Packard 197121   38 Mar 19 13:37 README
-rw-r--r-- 1 Hewlett Packard 197121  510 Mar 19 13:37 script.py.mako
(37venv)
Hewlett Packard@HP-Elitedesk-PC MINGW64 ~/OneDrive/Desktop/work/PythonCheatsheet/Engineering/37/db-migartion (37)
```

  - Update config for our project

Basically we need to update two files, alembic.ini and db_migration/env.py.

***alembic.ini***

```commandline
# sqlalchemy.url = driver://user:pass@localhost/dbname
sqlalchemy.url = mysql+mysqlconnector://rpython:Password-123@192.168.56.101:3306/db_migration
```

***db_migration/env.py***

```commandline
# from myapp import mymodel
# target_metadata = mymodel.Base.metadata
# target_metadata = None
from db_migration_models import Base
target_metadata = Base.metadata
```

  - Now you need to define your models. (Model entry script should be `db_migration_models` as we have imported above)

```python
from sqlalchemy.ext.declarative import declarative_base
import sqlalchemy as db

Base = declarative_base()


class Users(Base):
    """Employees Manager Model"""
    __tablename__ = 'users'
    emp_id = db.Column(db.Integer(), primary_key=True)
    emp_name = db.Column(db.String(50), nullable=False)

    # Representation
    def __repr__(self):
        return "<Managers: Id={}, Name={}>".format(self.emp_id, self.emp_name)
```

  - Create our migration

```commandline
$ alembic.exe revision --autogenerate -m "Initial Setup"
INFO  [alembic.runtime.migration] Context impl MySQLImpl.
INFO  [alembic.runtime.migration] Will assume non-transactional DDL.
INFO  [alembic.autogenerate.compare] Detected added table 'users'
Generating C:\Users\HP\OneDrive\Desktop\work\PythonCheatsheet\Engineering\37\db-migartion\db_migration\versions\a6630eb8a3c1_initial_setup.py ...  done
(37venv)
```

> In your RDBMS you will see alembic version table created.

```commandline
mysql> show tables;
+------------------------+
| Tables_in_db_migration |
+------------------------+
| alembic_version        |
+------------------------+
1 row in set (0.00 sec)

```

> Also in your filesystem you will see your migration script.

```commandline
$ ls -ltr db_migration/versions/
total 4
-rw-r--r-- 1 Hewlett Packard 197121 749 Mar 19 13:50 a6630eb8a3c1_initial_setup.py
(37venv)
```

  - Now we actually apply our migration to RDBMS
  
```commandline
$ alembic.exe upgrade heads
INFO  [alembic.runtime.migration] Context impl MySQLImpl.
INFO  [alembic.runtime.migration] Will assume non-transactional DDL.
INFO  [alembic.runtime.migration] Running upgrade  -> a6630eb8a3c1, Initial Setup
(37venv)
```

> In your RDBMS you will see tables created.

```commandline
mysql> show tables;
+------------------------+
| Tables_in_db_migration |
+------------------------+
| alembic_version        |
| users                  |
+------------------------+
2 rows in set (0.00 sec)

mysql> desc users;
+----------+-------------+------+-----+---------+----------------+
| Field    | Type        | Null | Key | Default | Extra          |
+----------+-------------+------+-----+---------+----------------+
| emp_id   | int         | NO   | PRI | NULL    | auto_increment |
| emp_name | varchar(50) | NO   |     | NULL    |                |
+----------+-------------+------+-----+---------+----------------+
2 rows in set (0.00 sec)
```

  - Now lets update our table.

> Below property added

```python
    emp_city = db.Column(db.String(50))
```

> Create a new migration

```commandline
$ alembic.exe revision --autogenerate -m "Update Users"
INFO  [alembic.runtime.migration] Context impl MySQLImpl.
INFO  [alembic.runtime.migration] Will assume non-transactional DDL.
INFO  [alembic.autogenerate.compare] Detected added column 'users.emp_city'
Generating C:\Users\HP\OneDrive\Desktop\work\PythonCheatsheet\Engineering\37\db-migartion\db_migration\versions\5aa57e606b4b_update_users.py ...  done
(37venv)

(37venv)
Hewlett Packard@HP-Elitedesk-PC MINGW64 ~/OneDrive/Desktop/work/PythonCheatsheet/Engineering/37/db-migartion (37)
$ ls -ltr db_migration/versions/
total 8
-rw-r--r-- 1 Hewlett Packard 197121 749 Mar 19 13:50 a6630eb8a3c1_initial_setup.py
-rw-r--r-- 1 Hewlett Packard 197121 677 Mar 19 14:05 5aa57e606b4b_update_users.py
(37venv)
Hewlett Packard@HP-Elitedesk-PC MINGW64 ~/OneDrive/Desktop/work/PythonCheatsheet/Engineering/37/db-migartion (37)
```

> Apply migration

```commandline
(37venv)
Hewlett Packard@HP-Elitedesk-PC MINGW64 ~/OneDrive/Desktop/work/PythonCheatsheet/Engineering/37/db-migartion (37)
$ alembic.exe upgrade heads
INFO  [alembic.runtime.migration] Context impl MySQLImpl.
INFO  [alembic.runtime.migration] Will assume non-transactional DDL.
INFO  [alembic.runtime.migration] Running upgrade a6630eb8a3c1 -> 5aa57e606b4b, Update Users
(37venv)
Hewlett Packard@HP-Elitedesk-PC MINGW64 ~/OneDrive/Desktop/work/PythonCheatsheet/Engineering/37/db-migartion (37)
```

> Check RDBMS

```commandline
mysql> desc users;
+----------+-------------+------+-----+---------+----------------+
| Field    | Type        | Null | Key | Default | Extra          |
+----------+-------------+------+-----+---------+----------------+
| emp_id   | int         | NO   | PRI | NULL    | auto_increment |
| emp_name | varchar(50) | NO   |     | NULL    |                |
| emp_city | varchar(50) | YES  |     | NULL    |                |
+----------+-------------+------+-----+---------+----------------+
3 rows in set (0.00 sec)
```

