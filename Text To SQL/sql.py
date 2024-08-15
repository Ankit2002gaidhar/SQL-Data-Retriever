import sqlite3

#Connect to sqlite
connection=sqlite3.connect("student.db")

## Create a cursor object to insert record ,create table retreieve
cursor=connection.cursor()

## Create the table

table_info="""
Create table STUDENT(NAME VARCHAR(25),CLASS VARCHAR(25),
SECTION VARCHAR(25),MARKS INT);
"""
cursor.execute(table_info)

## Insert records 

cursor.execute('''Insert Into STUDENT values('Rahul','Data Science','A',90)''')
cursor.execute('''Insert Into STUDENT values('Sudhanshu','Data Science','B',100)''')
cursor.execute('''Insert Into STUDENT values('Darwin','Data Science','A',86)''')
cursor.execute('''Insert Into STUDENT values('Vikash','DEVOPS','A',50)''')
cursor.execute('''Insert Into STUDENT values('Dipesh','DEVOPS','A',35)''')
cursor.execute('''Insert Into STUDENT values('Raj','Data Science','A',80)''')
cursor.execute('''Insert Into STUDENT values('Sudhir','Data Science','B',96)''')
cursor.execute('''Insert Into STUDENT values('Dario','Data Science','A',76)''')
cursor.execute('''Insert Into STUDENT values('Emilia','DEVOPS','A',46)''')
cursor.execute('''Insert Into STUDENT values('Jon','DEVOPS','A',39)''')

## Display all the records 
print("Inserted records are:")
data=cursor.execute('''Select * from STUDENT''' )

for row in data:
    print(row)

## Close the connection
connection.commit()
connection.close