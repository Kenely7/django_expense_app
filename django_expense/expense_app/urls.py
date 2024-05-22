from django.urls import path
from . import views


urlpatterns = [
    path("expenses/",views.list_expense),
    path("expenses/<int:pk>/",views.detail_expense),
    path("categories/", views.list_categories),
]

# endpoints

# expense = http://127.0.0.1:8001/expenses
# categories = http://127.0.0.1:8001/categories
# del_expenses = http://127.0.0.1:8001/expenses/id/