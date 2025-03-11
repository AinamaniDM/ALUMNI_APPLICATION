from django.urls import path
from . import views

app_name = 'activities'
urlpatterns = [
    path('', views.activity_list_view, name='activity_list'),
]