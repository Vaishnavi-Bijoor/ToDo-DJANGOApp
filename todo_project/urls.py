from django.contrib import admin
from django.urls import path,include
from accounts.views import register, login_view, logout_view
from tasks import views as task_views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', task_views.task_list, name='task_list'),
    path('add/', task_views.add_task, name='add_task'),
    path('edit/<int:pk>/', task_views.update_task, name='update_task'),
    path('delete/<int:pk>/', task_views.delete_task, name='delete_task'),

    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    
    path('', include('tasks.urls')),
]
