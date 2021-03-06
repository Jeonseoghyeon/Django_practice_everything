from django.contrib import admin
from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('signup/',views.signup,name='signup'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('delete_account/',views.delete_account,name='delete_account'),
    path('<username>/', views.profile, name='profile'),
    path('<username>/follow/',views.follow, name='follow'),
    ]