from django.urls import path
from . import views


urlpatterns = [
    path("expenses",views.list_expense),
]