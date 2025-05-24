from django.urls import path
from . import views

urlpatterns = [
    path("",views.task_list,name='task_list'),
    path('toggle/<int:pk>/',views.task_toggle,name='task_toggle'),
    path('delete/<int:pk>/',views.task_delete,name='task_delete'),
    path('edit/<int:pk>/',views.task_edit,name='task_edit'),
    path('signup/',views.signup,name='signup')
]