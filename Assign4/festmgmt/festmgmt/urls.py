from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('login/student/', views.student_login_view, name='student_login'),
    path('student_participated_events', views.student_participated_events_view, name='student_participated_events'),
    path('student_volunteered_events', views.student_volunteered_events_view, name='student_volunteered_events'),
    path('volunteer/<int:event_id>/', views.volunteer_event, name='volunteer_event'),
    path('participate/<int:event_id>/', views.participate_student_event, name='participate_student_event'),
    path('participate_event/<int:event_id>/', views.participate_event, name='participate_event'),
    path('unparticipate_event/<int:event_id>/', views.unparticipate_event, name='unparticipate_event'),
    path('unvolunteer_event/<int:event_id>/', views.unvolunteer_student_event, name='unvolunteer_event'),
    path('events/', views.events_view, name='events'),
    path('participated_events/', views.participated_events_view, name='participated_events'),
    path('login/organiser/', views.organiser_login_view, name='organiser_login'),
    path('login/organiser/add_winner/<int:event_id>/', views.add_winner, name='add_winner'),
    path('admin/', admin.site.urls),
    path('admin/', admin.site.index, name='adminview'),
    path('logout/', views.logout_view, name='logout'),
    path('create_event/', views.create_event_view, name='create_event')
    # Add more URL patterns as needed
]
