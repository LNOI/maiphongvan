from django.test import TestCase
from django.db import connection
# Create your tests here.

def Test():
    with connection.cursor() as cursor:
        cursor.execute("create tables account ( username varchar(100) )")
        
        cursor.execute("insert into account values ('nguyenthanh')")
        cursor.execute("select * from account")
        row=cursor.fetchall()
        print(row)
Test()