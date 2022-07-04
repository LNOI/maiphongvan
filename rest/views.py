from django.http import JsonResponse
from django.shortcuts import render
from django.db import connection
# Create your views here.
def home(request):
    return render(request,"./index.html",{})

def getdata(request):
    data={
        "name":"Nguyen Thanh Loi",
        "class":"University"
    }
    with connection.cursor() as cursor:
        cursor.execute("select * from account")
        row=cursor.fetchall()
        print(row)
    data={
        'data': row
    }
    return JsonResponse(data)