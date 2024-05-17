from django.urls import path
from . import views
urlpatterns = [
    path('register',views.register, name='register'),
    path('login',views.user_login, name='login'),
    path('dashboard',views.user_dashboard, name='dashboard'),
    path('logout', views.user_logout, name='logout'),
    path('update-user', views.update_user, name="update-user"),
    path('password-reset',views.password_reset, name='password-reset'),
]