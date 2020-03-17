from django.shortcuts import render
import json
from django.db import connection
cursor=connection.cursor()

# Create your views here.
def getData(request):
    result = []
    cursor.execute("select longitude lng,latitude lat,count(1) count from stat group by longitude,latitude")
    res = cursor.fetchall()
    desc = getList(cursor.description)
    for row in res:
        b = dict(zip(desc, row))
        result.append(b)
    result = json.dumps(result)
    print(result)
    return render(request,"../templates/strom_map.html",{"result":result})

def getList(desc):
    res = []
    for i in desc:
        res.append(i[0])
    return res