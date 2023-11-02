from django.urls import path
from . import views
from django.contrib import admin
from django.contrib.auth import views as auth_views


app_name = 'promo'

urlpatterns = [
    path('add_house/', views.add_house, name='add_house'),
    path('register/', views.register, name='register'),
    path('create_campaign/', views.create_campaign, name='create_campaign'),
    path('admin/', admin.site.urls),
    path('profile/', views.profile, name='profile'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('login/', auth_views.LoginView.as_view(template_name='promo/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', views.home, name='home'),
]