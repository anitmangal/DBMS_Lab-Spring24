from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('login/student/', views.student_login_view, name='student_login'),
    path('volunteer/<int:event_id>/', views.volunteer_event, name='volunteer_event'),
    path('events/', views.events_view, name='events'),
    path('login/organiser/', views.organiser_login_view, name='organiser_login'),
    # Add more URL patterns as needed
]
