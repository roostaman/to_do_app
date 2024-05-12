from django.urls import path, include
from . import views

urlpatterns = [
    path('addTask/', views.add_task, name='addTask'),
    path('markDone/<int:pk>/', views.mark_done, name='markDone'),
    path('deleteTask/<int:pk>/', views.delete_task, name='deleteTask'),
    path('editTask/<int:pk>/', views.edit_task, name='editTask'),
    path('markUndone/<int:pk>/', views.mark_undone, name='markUndone'),
]
