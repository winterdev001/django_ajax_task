from django.contrib.auth import views as auth_views
from django.urls import path, include
from . import views 

urlpatterns = [
    path('', auth_views.LoginView.as_view(template_name="auth/login.html"), name='root'),    
    path('register/', views.userRegister, name='register'),
    path('login/', views.userLogin, name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name="auth/logout.html"), name='logout'),

]