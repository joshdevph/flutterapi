from .views import todoList
from django.urls import path

urlpatterns = [
	path('', todoList.views)
]