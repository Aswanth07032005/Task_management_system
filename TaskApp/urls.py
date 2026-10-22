from django.urls import path
from . import views

urlpatterns = [
    #user
    path('', views.indexView, name='Home'),
    path('Register', views.RegisterView, name='RegisterF'),
    path('LoginV', views.LoginView, name='loginF'),
    path('Logout', views.LogOutView, name='logoutB'),

    #task
    path('create-task/', views.create_task, name='create_task'),
    path('tasks/', views.task_list, name='task_list'),
    path('toggle-task/<int:task_id>/',views.toggle_task_status,name='toggle_task_status'),
    path('edit-task/<int:task_id>/',views.edit_task,name='edit_task'),
    path('task-details/<int:task_id>/',views.task_detail,name='task_detail'),
    path('delete-task/<int:task_id>/', views.delete_task, name='delete_task'),

]