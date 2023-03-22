from django.shortcuts import render

# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response

from todo.models import Todo

class TodoAPI(APIView):
    def get(self, parms):
        todo = Todo.objects.all()
        res = {}
        res["todo"] = todo.values()

        return Response(data=res, status=200)

    def post(self, request):
        Todo(**request.data).save()
        return Response(data=request.data, status=200)

