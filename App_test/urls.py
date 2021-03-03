from django.urls import path
from App_test import views

app_name = 'App_test'

urlpatterns = [
    path('mcq', views.mutiple_choice_quiz, name='mcq'),
]
