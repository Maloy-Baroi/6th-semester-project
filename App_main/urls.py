from django.urls import path
from App_main import views

app_name = 'App_main'

urlpatterns = [
    path('routine', views.routine_sys, name='routine'),
    path('class-videos', views.class_video_sys, name='class-videos'),
    path('class-notes', views.class_notes_sys, name='class-notes'),
    path('profile', views.profile, name='profile'),
]
