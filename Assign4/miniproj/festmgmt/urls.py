from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('create-account/', views.create_account_view, name='create_account'),
    # Add more URL patterns as needed
]
