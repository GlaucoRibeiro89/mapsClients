from django.shortcuts import render
from django.http import *
from rest_framework.views import APIView
import MySQLdb

def index(request):
    if str(request.method) == 'GET':
        return render(request, 'index.html')
    else:
        return HttpResponseNotAllowed("NÃO PERMITIDO")

class getclients(APIView):
    def get(self, request):
        conn = MySQLdb.connect(host="172.16.80.200", user="root", password="marlon##ng134378", database="map_clients")
        try:
            cursor = conn.cursor()
            cursor.execute("select * from clients")
            rows = cursor.fetchall()
        finally:
            conn.close()
        return JsonResponse(rows, safe=False)
