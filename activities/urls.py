from django.urls import path
from . import views

app_name = 'activities_app'
urlpatterns = [
    path('', views.activity_list_view, name='activity_list'),
]