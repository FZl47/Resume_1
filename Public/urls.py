from django.urls import path
from . import views

app_name = 'Public'
urlpatterns = [
    path('',views.index)
]