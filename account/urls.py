from django.urls import path
from account import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    # path('login/', views.user_login, name="login")
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LoginView.as_view(), name='logout'),

]