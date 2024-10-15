from django.urls import path
from .views import views

urlpatterns = [
    path('', views.display_users, name='user_management')
]