from django.contrib import admin
from django.urls import path, include
from .import views


urlpatterns = [
    path('delete/<int:taskid>/',views.delete,name="delete"),
    path('update/<int:id>/',views.update,name="update"),
    path('cbv/',views.TaskListView.as_view(),name="cbv"),
    path('cbvdetail/<int:pk>/',views.TaskDetailView.as_view(),name="cbvdetail"),
    path('cbvupdate/<int:pk>/',views.TaskUpdateView.as_view(),name="cbvupdate"),
    path('cbvdelete/<int:pk>/',views.TaskDeleteView.as_view(),name="cbvdelete"),

    path('',views.task_view,name="task_view"),
]