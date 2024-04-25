from rest_framework import serializers
from .models import Category,Expense




class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name"]


class ExpenseSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only = True)
    category_id = serializers.IntegerField

    class Meta:
        model = Expense
        fields = ["id","description","category","amount", "category_id"]


