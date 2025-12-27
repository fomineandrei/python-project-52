from django.urls import path

from task_manager.tasks import views

urlpatterns = [
    path('', views.IndexTasksView.as_view(), name='index_tasks'),
    path('create/', views.CreateTaskView.as_view(), name='create_task'),
    path('<int:pk>/update/',
         views.UpdateTaskView.as_view(), name='update_task'),
    path('<int:pk>/delete/',
         views.DeleteTaskView.as_view(), name='delete_task'),
    path('<int:pk>/', views.InfoTaskView.as_view(), name='info_task')
]