from django.urls import path

from task_manager.users import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index_users'),
    path('create/', views.CreateUserView.as_view(), name='create_user'),
    path('update/', views.UpdateUserView.as_view(), name='update_user'),
    path('delete/', views.DeleteUserView.as_view(), name='delete_user'),
    path('login/', views.LoginUserView.as_view(), name='login_user'),
    path('logout/', views.LogoutUserView.as_view(), name='logout_user')
]