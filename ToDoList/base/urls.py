from django.contrib import admin
from django.urls import path
from django.urls import include
from . import views
urlpatterns = [
    path('', views.Home, name="todo-home"),
    path('<int:pk>/update', views.editToDo.as_view(), name='todo-update'),
    path('<int:pk>/delete', views.deleteToDo.as_view(), name='todo-delete')
]
