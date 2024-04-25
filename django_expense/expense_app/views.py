from django.shortcuts import render
from.models import Expense,Category
from .serializers import ExpenseSerializer,CategorySerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
# Create your views here.



@api_view(["GET","POST"])
def list_expense(request):
    if request.method =="GET":      
        expenses = Expense.objects.all()
        serializer = ExpenseSerializer(expenses, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer= ExpenseSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)